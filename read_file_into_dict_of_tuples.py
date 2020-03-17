#!/usr/bin/env python
from pprint import pprint

knight_info = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        line = raw_line.rstrip()  # nuke the \n
        name, title, color, quest, comment = line.split(':')
        knight_info[name] = title, color, quest, comment

pprint(knight_info)

print(knight_info['Galahad'][2], '\n')

for knight, data in knight_info.items():
    print(data[0], knight)

