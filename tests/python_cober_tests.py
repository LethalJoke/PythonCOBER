import unittest
from python_cober.analysis.number_analysis import cober_from_number_to_string


class PythonCoberTests(unittest.TestCase):

    def test_when_number_is_not_divisible_by_three_or_five_should_print_number(self):
        self.assertEqual(cober_from_number_to_string(1), '1', "Should be '1'")


if __name__ == '__main__':
    unittest.main()
