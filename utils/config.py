""" Configuration properties defined here"""
import os
from utils import string_utils

PORT = int(os.environ.get("PORT", 5000))
# Property name in entities in incoming data that contains url to file to be downloaded
FILE_URL = os.environ.get('FILE_URL', 'file_url')
# property name in entities in incoming data that contains name  of file to be downloaded
FILE_NAME = os.environ.get('FILE_NAME', 'file_id')
# Chunk size for file upload = 10 MB
CHUNK_SIZE = os.environ.get('CHUNK_SIZE', 262144 * 4 * 10)
# URL where to upload parsed plain text result
UPLOAD_URL = os.environ.get('UPLOAD_URL')
# application log level
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
# If request should fail and return when parsing or other error occurs
FAIL_ON_ERROR = string_utils.str_to_bool(os.environ.get("FAIL_ON_ERROR", "True"))
# Which OCR language to use may be eng, nor or eng+nor, note that you need Tika version 1.20+
# to use multiple languages
TESSERACT_OCR_LANG = os.environ.get("TESSERACT_OCR_LANG", "eng+nor")
# if Tika will try to extract text from inline PDF images (more RAM and CPU consuming)
# must be in low cap string form true/false
PDF_EXTRACT_INLINE_IMG = os.environ.get("PDF_EXTRACT_INLINE_IMG", "true")

PRESERVE_FILE_TYPE = string_utils.str_to_bool(os.environ.get("PRESERVE_FILE_TYPE", "False"))
