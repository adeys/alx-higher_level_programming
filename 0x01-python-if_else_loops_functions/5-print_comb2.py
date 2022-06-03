#!/usr/bin/python3
for i in range(0, 100):
    if i == 99:
        print(i)
    else:
        print(f"{i:0>2d}", end=", ")
