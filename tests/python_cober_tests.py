import unittest
from python_cober.analysis.number_analysis import cober_from_number_to_string


class PythonCoberTests(unittest.TestCase):

    def test_when_number_is_not_divisible_by_three_or_five_should_print_number(self):
        self.assertEqual(cober_from_number_to_string(1), '1', "Should be '1'")

    def test_when_number_is_not_divisible_by_three_and_not_five_should_print_co(self):
        self.assertEqual(cober_from_number_to_string(3), 'co', "Should be 'co'")

    def test_when_number_is_not_divisible_by_five_and_not_three_should_print_ber(self):
        self.assertEqual(cober_from_number_to_string(5), 'ber', "Should be 'ber'")

    def test_when_number_is_not_divisible_by_three_and_five_should_print_cober(self):
        self.assertEqual(cober_from_number_to_string(15), 'cober', "Should be 'cober'")

if __name__ == '__main__':
    unittest.main()
