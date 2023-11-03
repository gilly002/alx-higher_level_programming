#!/usr/bin/python3
for i in range(9):
    for q in range(i + 1, 10):
        if i * 10 + q < 89:
            print("{:d}{:d}".format(i, q), end=", ")
print("{:d}".format(89))
