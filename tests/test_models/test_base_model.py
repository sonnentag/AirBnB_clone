#!/usr/bin/python3
""" BaseModel Unit Test Module """
import unittest
import pep8
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """ BaseModel Unit tests """

    @classmethod
    def setUp(cls):
        cls.base1 = BaseModel()

    @classmethod
    def tearDown(cls):
        del cls.base1
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_pep8(self):
        """ pep8 test """

        style = pep8.StyleGuide(quiet=True)
        p8 = style.check_files(['models/base_model.py'])
        self.assertEqual(p8.total_errors, 0, "pep8 errors")

    def test_init(self):
        self.assertNotEqual(self.base1.created_at, self.base1.updated_at)


if __name__ == "__main__":
    unittest.main()
