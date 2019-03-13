"""
Data processing functions
"""
import logging
from tika import parser, tika


def process_file(path):
    """
    Function that processes local file
    :param path: path to file
    :return:  parsed metadata and hopefully file content
    """
    tika.TikaVersion = '1.20'
    tika.log.setLevel(logging.DEBUG)
    headers = {
        "X-Tika-OCRLanguage": "eng+nor",
        "X-Tika-PDFextractInlineImages": "true"
    }
    parsed = parser.from_file(path, headers=headers)
    return parsed
