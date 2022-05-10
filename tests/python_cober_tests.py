import unittest
from python_cober.analysis.number_analysis import cober_from_number_to_string, cober_from_number_list_to_string_list


class PythonCoberTests(unittest.TestCase):

    def test_when_number_is_not_divisible_by_three_or_five_should_return_number(self):
        self.assertEqual('1', cober_from_number_to_string(1), "Should be '1'")

    def test_when_number_is_not_divisible_by_three_and_not_five_should_return_co(self):
        self.assertEqual('CO', cober_from_number_to_string(3), "Should be 'CO'")

    def test_when_number_is_not_divisible_by_five_and_not_three_should_return_ber(self):
        self.assertEqual('BER', cober_from_number_to_string(5),"Should be 'BER'")

    def test_when_number_is_not_divisible_by_three_and_five_should_return_cober(self):
        self.assertEqual('COBER', cober_from_number_to_string(15), "Should be 'COBER'")

    def test_when_list_used_on_cober_function_should_return_proper_output(self):
        input_list = [1, 3, 5, 15, 13]
        expected_output = ['1', 'CO', 'BER', 'COBER', '13']
        self.assertEqual(expected_output, cober_from_number_list_to_string_list(input_list), "Should be " + str(expected_output))

    def test_when_list_with_negative_numbers_used_on_cober_function_should_return_proper_output(self):
        input_list = [-15, -3, -95, -7, 653]
        expected_output = ['COBER', 'CO', 'BER', '-7', '653']
        self.assertEqual(expected_output, cober_from_number_list_to_string_list(input_list), "Should be " + str(expected_output))

    def test_when_number_has_an_invalid_value_should_raise_valueerror_exception(self):
        self.assertRaises(ValueError, cober_from_number_to_string, -1999)

    def test_when_list_contains_number_with_invalid_value_should_raise_valueerror_exception(self):
        input_list = [-15, -3, -95, -7, 1653]
        self.assertRaises(ValueError, cober_from_number_list_to_string_list, input_list)


if __name__ == '__main__':
    unittest.main()
