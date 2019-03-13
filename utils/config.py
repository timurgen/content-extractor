""" Configuration properties defined here"""
import os


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
