import unittest
from unittest import mock

from oop2 import Card


class TestCheckValid(unittest.TestCase):


    def test_cn_not_valid(self):
        card = Card(
            11111111111,
            "Test",
            12,
            2100,
            293,
            "Test"
        )
        with self.assertRaises(Exception):
            card.check_valid()

    @mock.patch.object(Card, "check_number")
    def test_year_invalid(self, check_number):
        check_number.return_value = True
        card = Card(
            11111111111,
            "Test",
            12,
            2000,
            293,
            "Test"
        )
        self.assertFalse(card.check_valid())

    @mock.patch.object(Card, "check_number")
    def test_month_invalid(self, check_number):
        check_number.return_value = True
        card = Card(
            11111111111,
            "Test",
            5,
            2100,
            293,
            "Test"
        )
        self.assertFalse(card.check_valid())

if __name__ == "__main__":
    unittest.main()