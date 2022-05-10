
def cober_from_number_to_string(value):
    return_val = ''
    if value % 3 == 0:
        return_val += 'co'
    return str(value) if return_val == '' else return_val
