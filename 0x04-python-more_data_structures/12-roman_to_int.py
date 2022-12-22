#!/usr/bin/python3

def roman_to_int(roman_string):
    if not roman_string or not isinstance(roman_string, str):
        return 0

    map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    substr = {'V': 'I', 'X': 'I', 'L': 'X', 'C': 'X', 'D': 'C', 'M': 'C'}
    substr_keys = list(substr)
    prev, value = None, 0
    for i in roman_string:
        value += map[i]
        if i in substr_keys and prev == substr[i]:
            value -= 2 * map[prev]
        prev = i

    return value
