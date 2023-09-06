#!/usr/bin/python3
'''prints a string in uppercase followed by a new line'''

def uppercase(str):
    for i in str:
        letter = ord(i)
        if letter > 96 and letter < 123:
            letter -= 32
        print("{}".format(chr(letter)), end='')
    print("")
