#!/usr/bin/python3

def uniq_add(my_list=[]):
    used, total = [], 0
    for n in my_list:
        if n not in used:
            total += n
            used.append(n)

    return total
