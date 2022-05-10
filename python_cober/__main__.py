import sys
from analysis.number_analysis import cober_from_number_list_to_string_list

if __name__ == '__main__':
    list_values = list(map(int, sys.argv[1:]))
    print(cober_from_number_list_to_string_list(list_values))