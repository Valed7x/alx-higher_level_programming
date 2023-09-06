#!/usr/bin/python3
'''program that prints the ASCII alphabet, in reverse order, alternating lowercase and uppercase (z in lowercase and Y in uppercase) , not followed by a new line.'''

for i in reversed(range(26)):
    letter = 0
    if i % 2 == 1:
        letter = letter + i + 97
    else:
        letter = letter + i + 65
    print("{}".format(chr(letter)), end='')
