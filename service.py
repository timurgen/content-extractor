"""
Content extractor service
Uses Apache Tika and Tesseract OCR libraries to extract content from different types of file
"""
import os
import io
import json
import tempfile

from pathlib import Path

import cherrypy
import requests

from flask import Flask, request, Response
from werkzeug.exceptions import BadRequest, InternalServerError
from utils import logging, file_utils, exceptions, config
from service import processor

LOGGER = logging.get_logger("main", config.LOG_LEVEL)

APP = Flask(__name__)
exceptions.JSONExceptionHandler(APP)


@APP.route("/post_file_list", methods=["POST"])
def post_file_list():
    """
    Upload one or more files and return parsed result back as JSON array
    :return:
    """
    files = request.files

    if not files:
        LOGGER.info("No file found in request")
        raise BadRequest("No file found in request")

    result = []

    for file in files:

        if not files[file] or not file_utils.allowed_file(files[file]):
            LOGGER.info("No file or file not allowed")
            raise BadRequest("No file or file not allowed")

        with tempfile.NamedTemporaryFile(mode='r+b', delete=False) as temp_file_ptr:
            temp_file_ptr.write(files[file].read())
            temp_file_ptr.flush()
            os.fsync(temp_file_ptr)
            temp_file_ptr.close()
            result.append(processor.process_file(temp_file_ptr.name))
            os.remove(temp_file_ptr.name)

    return Response(
        json.dumps(result), mimetype='application/json')


@APP.route("/post_json_list", methods=["POST"])
def post_json_list():
    """
    Takes JSON array with one or more objects containing URL's for direct file download,
    download files, parse them and upload to another place as plain text if UPLOAD_URL is defined
    or returned back as JSON array otherwise
    :return:
    """
    input_data = request.get_json()

    for input_entity in input_data:
        file_url = input_entity[config.FILE_URL]
        file_name = input_entity[config.FILE_NAME]
        local_path = input_entity.get('local_path')

        LOGGER.info("processing request for %s", file_name)
        file_path = None
        try:
            LOGGER.info("download file %s", file_name)
            res = requests.get(file_url, stream=True)
            res.raise_for_status()
            file_path = file_utils.download_file(res)
            parsed_file = processor.process_file(file_path)

            if parsed_file["status"] and parsed_file["status"] == 200:
                LOGGER.info("Successfully parsed %s", file_name)
            else:
                raise Exception("Parsed file status not ok: {}".format(parsed_file))
            if config.UPLOAD_URL:
                headers = {}
                if local_path:
                    headers["local_path"] = local_path

                LOGGER.debug("Starting upload file %s to %s", file_name, config.UPLOAD_URL)

                file_like_obj = io.StringIO(parsed_file['content'])

                if config.PRESERVE_FILE_TYPE:
                    file_name += ".txt"
                else:
                    path = Path(file_name)
                    file_name = str(path.with_suffix('.txt'))
                requests.post(config.UPLOAD_URL,
                              files={file_name: (file_name, file_like_obj)},
                              headers=headers)
                LOGGER.debug("File %s uploaded", file_path)
                input_entity['transfer_service'] = "PARSED AND TRANSFERRED"

            input_entity['parsed_data'] = parsed_file
        except Exception as exc:
            LOGGER.warning("Error occurred: %s", exc)
            if config.FAIL_ON_ERROR:
                raise InternalServerError(exc)
            input_entity['transfer_service'] = "ERROR: {}".format(str(exc))
        finally:
            if file_path:
                LOGGER.debug("Deleting temporary file %s", file_path)
                os.remove(file_path)
    return Response(json.dumps(input_data), content_type='application/json')


if __name__ == '__main__':
    cherrypy.tree.graft(APP, '/')
    cherrypy.config.update({
        'environment': 'production',
        'engine.autoreload_on': True,
        'log.screen': True,
        'server.socket_port': config.PORT,
        'server.socket_host': '0.0.0.0',
        'server.thread_pool': 10
    })

    cherrypy.engine.start()
    cherrypy.engine.block()
