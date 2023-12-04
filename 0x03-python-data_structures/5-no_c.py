#!/usr/bin/python3
def no_c(my_string):
    copy = [p for p in my_string if p != 'c' and p != 'C']
    return ("".join(copy))
