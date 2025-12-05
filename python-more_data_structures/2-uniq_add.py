#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_set = set(my_list)
    total = 0
    for n in unique_set:
        total += n
    return total
