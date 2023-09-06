#!/usr/bin/python3
'''prints all possible different combinations of two digits.'''

for a in range(0, 9):
    for k in range(a + 1, 10):
        if a != 8:
            print("{0}{1}, ".format(a, k), end='')
        else:
            print("{0}{1}".format(a, k))
