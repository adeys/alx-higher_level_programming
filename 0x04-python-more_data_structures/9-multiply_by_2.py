#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = dict()
    for i in list(a_dictionary):
        new_dict[i] = a_dictionary[i] * 2

    return new_dict
