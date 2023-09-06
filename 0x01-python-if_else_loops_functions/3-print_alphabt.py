#!/usr/bin/python3
'''that prints the ASCII alphabet, in lowercase, not followed by a new line.'''

for letter in range(97, 123):
    if letter != 101 and letter != 113:
        print("{}".format(chr(letter)), end='')
