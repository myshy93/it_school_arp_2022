import unittest

from main import ATM
# TestCase

class TestConstructor(unittest.TestCase):

    def test_pin_value(self):
        atm = ATM()
        self.assertEqual(atm.pin, "8464903")