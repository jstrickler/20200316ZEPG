#!/usr/bin/env python
from pprint import pprint

letter_counts = {}

with open('DATA/words.txt') as words_in:
    for word in words_in:
        first_letter = word[0]

        if first_letter not in letter_counts:
            letter_counts[first_letter] = 0

        letter_counts[first_letter] += 1

pprint(letter_counts)

def by_value(item):
    return item[1], item[0]

for letter, count in sorted(letter_counts.items(), key=by_value, reverse=True):
    print(letter, count)
