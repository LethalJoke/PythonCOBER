import unittest
from python_cober.analysis.number_analysis import cober_from_number_to_string, cober_from_number_list_to_string_list


class PythonCoberTests(unittest.TestCase):

    def test_when_number_is_not_divisible_by_three_or_five_should_return_number(self):
        self.assertEqual(cober_from_number_to_string(1), '1', "Should be '1'")

    def test_when_number_is_not_divisible_by_three_and_not_five_should_return_co(self):
        self.assertEqual(cober_from_number_to_string(3), 'co', "Should be 'co'")

    def test_when_number_is_not_divisible_by_five_and_not_three_should_return_ber(self):
        self.assertEqual(cober_from_number_to_string(5), 'ber', "Should be 'ber'")

    def test_when_number_is_not_divisible_by_three_and_five_should_return_cober(self):
        self.assertEqual(cober_from_number_to_string(15), 'cober', "Should be 'cober'")

    def test_when_list_used_on_cober_function_should_return_proper_output(self):
        input_list = [1, 3, 5, 15, 13]
        expected_output = ['1', 'co', 'ber', 'cober', '13']
        self.assertEqual(cober_from_number_list_to_string_list(input_list), expected_output, "Should be " + str(expected_output))

    def test_when_list_with_negative_numbers_used_on_cober_function_should_return_proper_output(self):
        input_list = [-15, -3, -95, -7, 653]
        expected_output = ['cober', 'co', 'ber', '-7', '653']
        self.assertEqual(cober_from_number_list_to_string_list(input_list), expected_output, "Should be " + str(expected_output))


if __name__ == '__main__':
    unittest.main()
