#!/usr/bin/env python

x = 100  # GLOBAL


def spam(thing):
    x = 42
    print("thing:", thing)
    thing = 8
    print("thing:", thing)
    print("spam(): x is", x)
    animal = 'wombat'  # LOCAL

m = 1000
spam(m)
# print("animal is", animal)
print("main: x is", x)
print("m is", m)
