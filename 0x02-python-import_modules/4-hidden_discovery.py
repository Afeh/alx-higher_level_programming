#!/usr/bin/python3

if __name__ == "__main__":
    hidden = __import__("hidden_4")
    print(*[name for name in dir(hidden) if not name.startswith("__")], sep="\n")
