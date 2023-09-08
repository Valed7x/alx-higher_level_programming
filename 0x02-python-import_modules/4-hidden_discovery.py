#!/usr/bin/python3
'''Write a program that prints all the names defined by the compiled module'''

import hidden_4

if __name__ == "__main__":
    names = dir(hidden_4)
    for name in names:
        if not name[:2] == "__":
            print(name)
