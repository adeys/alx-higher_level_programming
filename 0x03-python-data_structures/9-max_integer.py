#!/usr/bin/python3

def max_integer(my_list=[]):
	size = len(my_list)

    if size == 0:
        return "None"
    else:
        max = my_list[0]
        for i in range(size):
            if my_list[i] > max:
                max = my_list[i]
        return max
