#!/usr/bin/python3
'''that prints the ASCII alphabet, in lowercase, not followed by a new line.'''

for i in range(ord('a'), ord('z') + 1):
    if i != ord('e') and i != ord('q'):
        print('{}'.format(chr(i)), end='')
