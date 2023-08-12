#!/usr/bin/python3

if __name__ == '__main__':
    hidden = __import__('hidden_4')
    filtered_names = [name for name in dir(hidden) if not name.startswith("__")]
    sorted_names = sorted(filtered_names)

    for name in sorted_names:
        print(name)
