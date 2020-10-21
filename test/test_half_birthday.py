import unittest

from more_fun_with_collections import half_birthday

from datetime import datetime


class MyTestCase(unittest.TestCase):
    def test_half_birthday(self):
        self.assertEqual(datetime(2021, 1, 17), half_birthday.half_birthday(2020, 7, 19))


if __name__ == '__main__':
    unittest.main()
