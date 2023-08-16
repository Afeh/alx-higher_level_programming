#!/usr/bin/python3
import hidden_4

def finder():
    for k in dir(hidden_4):
        if not (k[0] == '_' and k[1] == '_'):
            print(k)


if __name__ == "__main__":
    finder()