#!/usr/bin/python3

def complex_delete(a_dictionary, value):

    while value in a_dictionary.values():
        for p, y in a_dictionary.items():
            if y == value:
                del a_dictionary[p]
                break

    return (a_dictionary)
