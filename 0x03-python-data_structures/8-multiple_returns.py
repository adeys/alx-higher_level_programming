#!/usr/bin/python3

def multiple_returns(sentence):
    length = len(sentence)
    return length, None if length == 0 else sentence[0]
