#!/usr/bin/env python

limit = 101

flags = [True] * limit

# print(flags)

for num in range(2, limit):
    if flags[num]:
        print(num)
        for multiple in range(num * 2, limit, num):
            flags[multiple] = False

