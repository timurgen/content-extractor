from utils.file_utils import allowed_file, config

from unittest import TestCase


class TestAllowedFile(TestCase):
    def test_allowed_file_1(self):
        config.ALLOWED_FILE_TYPES = '.pdf'
        self.assertTrue(allowed_file("test.pdf"))

    def test_allowed_file_2(self):
        config.ALLOWED_FILE_TYPES = '.pdf'
        self.assertFalse(allowed_file("test.exe"))

    def test_allowed_file_3(self):
        config.ALLOWED_FILE_TYPES = ('.pdf', '.txt')
        self.assertTrue(allowed_file("test.docx.pdf"))

    def test_allowed_file_4(self):
        config.ALLOWED_FILE_TYPES = ('.pdf', '.txt')
        self.assertFalse(allowed_file("test.exe"))
