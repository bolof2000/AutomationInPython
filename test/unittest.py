import unittest

class TestCaseDemo(unittest.TestCase):

    def setUp(self):

        print("I will run once before every test")

    def test_method(self):

        print("running method A")

    def tearDown(self):

        print("I will run after every test")

