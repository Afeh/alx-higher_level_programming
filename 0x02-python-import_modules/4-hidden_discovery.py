#!/usr/bin/python3
import hidden_4


def finder():
    dir_name = dir(hidden_4)
    for k in dir_name:
        if k[:2] != '__':
            print("{:s}".format(k))

if __name__ == "__main__":
    finder()
