#!/usr/bin/env python

fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

with open('fruitdata.txt', 'w') as fruitdata_out:
    for fruit in sorted(fruits):
        fruitdata_out.write(fruit + '\n')

with open('fruitdata.txt') as fruitdata_in:
    with open('fruittitle.txt', 'w') as fruittitle_out:
        for fruit in fruitdata_in:
            fruittitle_out.write(fruit.title())

