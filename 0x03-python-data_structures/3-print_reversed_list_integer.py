#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    reverse_list = []

    if isinstance(my_list, list):
        for element in my_list:
            reverse_list.insert(0, element)
        for number in reverse_list:
            print("{:d}".format(number))
