#!/usr/bin/env python


# file_name = '\blah\new\tech\repo\foo.txt'
file_name = '/blah/new/tech/repo/foo.txt'

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:
        line = raw_line.rstrip()
        print(line)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()
    print("RAW:")
    print(repr(contents))
    print("COOKED:")
    print(contents)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = [line.rstrip() for line in mary_in]
    print(all_lines_without_nl)
print('-' * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print('-' * 60)


with open('DATA/words.txt') as words_in:
    words = [line.rstrip() for line in words_in]
    print(words[:50])
print('-' * 60)

