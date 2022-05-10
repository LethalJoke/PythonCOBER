
def cober_from_number_to_string(value):
    return_val = ''

    if value % 3 == 0:
        return_val += 'CO'
    if value % 5 == 0:
        return_val += 'BER'

    return str(value) if return_val == '' else return_val


def cober_from_number_list_to_string_list(list_values):
    return [cober_from_number_to_string(value) for value in list_values]
