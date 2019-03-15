from .string_utils import str_to_bool

from unittest import TestCase


class TestStrToBool(TestCase):
    def test_str_to_bool_1(self):
        self.assertTrue(str_to_bool("true"))

    def test_str_to_bool_2(self):
        self.assertTrue(str_to_bool("True"))

    def test_str_to_bool_3(self):
        self.assertFalse(str_to_bool(1))

    def test_str_to_bool_4(self):
        self.assertFalse(str_to_bool(""))

    def test_str_to_bool_5(self):
        self.assertFalse(str_to_bool("false"))

    def test_str_to_bool_5(self):
        self.assertFalse(str_to_bool("stranger things"))
