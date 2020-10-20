import unittest
from more_fun_with_collections import dict_membership


class MyTestCase(unittest.TestCase):
    def test_in_dict_true(self):
        self.assertEqual(True, dict_membership.in_dict({3, 4, 5, 6, 7}, 5))

    def test_in_dict_false(self):
        self.assertEqual(False, dict_membership.in_dict({'A'}, 5))


if __name__ == '__main__':
    unittest.main()
