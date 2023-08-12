#!/usr/bin/python3

if __name__ == "__main__":
    hidden_names = [name for name in dir(__import__("hidden_4")) if not name.startswith("__")]
    print(*hidden_names, sep="\n")
