#!/usr/bin/python3

import hidden_4

def main():
    module_names = [name for name in dir(hidden_4) if not name.startswith("__")]
    print(*module_names, sep="\n")

if __name__ == "__main__":
    main()