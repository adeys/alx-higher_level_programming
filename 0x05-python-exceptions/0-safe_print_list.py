#!/usr/bin/python3

def safe_print_list(my_list=[], x=10):
    length = x
    for i in range(x):
        try:
            print(my_list[i], end="")
        except Exception:
            length = i - 1

    print("")
    return length
