#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list or len(my_list) == 0:
        return 0

    num = 0
    den = 0
    for tp in my_list:
        num += tp[0] * tp[1]
        den += tp[1]

    return num / den
