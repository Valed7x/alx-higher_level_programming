#!/usr/bin/python3
'''Write a function that checks for lowercase character.'''

def islower(c):
    if ord(c) < 97 or ord(c) > 122:
        return False
    return True
