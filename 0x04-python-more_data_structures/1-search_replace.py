#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for n in my_list:
        new_list.append(replace if n == search else n)

    return new_list
