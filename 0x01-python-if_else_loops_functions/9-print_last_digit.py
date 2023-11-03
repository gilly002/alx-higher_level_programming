#!/usr/bin/python3
def print_last_digit(num):
    if num < 0:
        last_num = (-num % 10)
    elif num >= 0:
        last_num = num % 10
    print("{:d}".format(last_num), end="")
    return last_num
