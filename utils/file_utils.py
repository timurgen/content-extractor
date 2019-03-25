"""
Different file utils functions
"""
import tempfile
from utils import logging, config

LOGGER = logging.get_logger("file-utils", config.LOG_LEVEL)


def allowed_file(file_name: str) ->bool:
    """
    return true if file  type is allowed
    :param file_name:
    :return: True if file extension is listed in config.ALLOWED_FILE_TYPES or False otherwise
    """
    return file_name.lower().endswith(config.ALLOWED_FILE_TYPES)


def download_file(res):
    """
    Download file into temporary file
    :param res: Response object
    :return: downloaded file location
    """
    LOGGER.debug("Chunked file download started")
    with tempfile.NamedTemporaryFile(delete=False) as file:
        for chunk in res.iter_content(chunk_size=config.CHUNK_SIZE):
            if chunk:
                file.write(chunk)
        file.close()
    LOGGER.debug("File stored as %s", file.name)
    return file.name
