#!/usr/bin/env python
from pprint import pprint


def main():
    d = read_data()
    pretty_print(d)
    print()
    print(get_field_value(d, 'Arthur', 2))
    print()
    print_titles(d)


def read_data():
    knight_info = {}

    with open('DATA/knights.txt') as knights_in:
        for raw_line in knights_in:
            line = raw_line.rstrip()  # nuke the \n
            name, title, color, quest, comment = line.split(':')
            knight_info[name] = title, color, quest, comment
    return knight_info


def pretty_print(info):
    pprint(info)


def get_field_value(info, knight, field):
    return info[knight][field]


def print_titles(info):
    for knight, data in info.items():
        print(data[0], knight)


if __name__ == '__main__':  # if I'm a script, not a module
    main()

