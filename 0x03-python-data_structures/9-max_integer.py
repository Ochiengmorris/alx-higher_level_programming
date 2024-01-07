#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return (None)
    min_value = -10000000
    for i in my_list:
        if i > min_value:
            min_value = i
    return (min_value)
