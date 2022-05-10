from python_cober.utils.constants import MIN_LIST_INT, MAX_LIST_INT


def cober_from_number_to_string(value):
    """
        Returns a COBER string.

        Parameters:
            value (int) : An int to evaluate. Must be

        Returns:
            cober_from_number_to_string(value) : A COBER string corresponding to that value.
    """

    if value < MIN_LIST_INT or value > MAX_LIST_INT:
        raise ValueError("The value of one of the list's numbers is either higher than 1000 or lower than -1000")

    return_val = ''

    if value % 3 == 0:
        return_val += 'CO'
    if value % 5 == 0:
        return_val += 'BER'

    return str(value) if return_val == '' else return_val


def cober_from_number_list_to_string_list(list_values):
    """
            Returns a list of COBER strings.

            Parameters:
                list_values (list(int)) : A list of ints to evaluate.

            Returns:
                cober_from_number_list_to_string_list(list_values) : A COBER string list corresponding to list_values.
        """
    return [cober_from_number_to_string(value) for value in list_values]
