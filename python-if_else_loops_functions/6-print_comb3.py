#!/usr/bin/python3
for num in range(0, 10):
    for pos in range(0, 10):
        if num >= pos:
            pass
        else:
            print("{}{}".format(num, pos), end=", ")
