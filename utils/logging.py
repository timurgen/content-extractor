"""
Simple JSON log formatter
"""
import logging
import json
import io
import traceback


class JsonFormatter(logging.Formatter):
    """
    Simple JSON log formatter
    """
    def formatException(self, ei):
        """
        Function to format exceptions
        :param ei: exception information
        :return: JSONized exception info
        """
        sio = io.StringIO()
        traceback.print_exception(ei[0], ei[1], ei[2], None, sio)
        message = sio.getvalue()
        res_obj = {"exc_info": message}
        return json.dumps(res_obj)

    def formatStack(self, stack_info):
        """
        Function to format stack traces as JSON
        :param stack_info:
        :return:
        """
        return json.dumps({"stack_info": stack_info})

    def format(self, record):
        """
        Function to format log records using JSON formatter
        :param record:
        :return:
        """
        message = super(JsonFormatter, self).format(record)
        return message


FORMAT_STRING = '{' \
                '"timestamp": "%(asctime)s", ' \
                '"logger-name": "%(name)s", ' \
                '"logging-level": "%(levelname)s", ' \
                '"message": "%(message)s"}'

# Log to stdout
STDOUT_HANDLER = logging.StreamHandler()
STDOUT_HANDLER.setFormatter(JsonFormatter(FORMAT_STRING))


def get_logger(name: str, level=logging.INFO):
    """
    Simple log init function
    :param name: logger name
    :param level: logging level
    :return: logger
    """
    logger = logging.getLogger(name)
    logger.addHandler(STDOUT_HANDLER)
    logger.propagate = False
    logger.setLevel(level)
    return logger
