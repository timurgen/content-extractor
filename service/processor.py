"""
Data processing functions
"""
import logging
from utils import config
from tika import parser, tika


def process_file(path):
    """
    Function that processes local file
    :param path: path to file
    :return:  parsed metadata and hopefully file content
    """
    headers = {
        "X-Tika-OCRLanguage": config.TESSERACT_OCR_LANG,
        "X-Tika-PDFextractInlineImages": config.PDF_EXTRACT_INLINE_IMG
    }
    parsed = parser.from_file(path, headers=headers)
    return parsed
