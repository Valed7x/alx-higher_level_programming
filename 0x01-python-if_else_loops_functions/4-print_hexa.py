#!/usr/bin/python3
'''prints all numbers from 0 to 98 in decimal and in hexadecimal'''

for num in range(0, 99):
    print('{0} = {1}'.format(num, hex(num)))
