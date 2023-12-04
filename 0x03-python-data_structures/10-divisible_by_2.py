#!/usr/bin/python3
def divisible_by_2(my_list=[]):

    newlist = []
    p = len(my_list)

    for i in range(p):
        if my_list[i] % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)
    return newlis
