#!/usr/bin/env python

colors = ["red", "blue", "green", "yellow", "brown", "black"]
months = (
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec",
)

print("colors: len is {}; min is {}; max is {}".format(len(colors), min(colors), max(colors)))
print("months: len is {}; min is {}; max is {}".format(len(months), min(months), max(months)))
print()

print("sorted:", end=' ')
for m in sorted(colors):   # <1>
    print(m, end=' ')
print()

phrase = ('dog', 'bites', 'man')
rev = reversed(phrase)  # rev is a GENERATOR
print(rev)  # <2>
for word in rev:
    print(word)
print()

first_names = "Bill Bill Dennis Steve Larry".split()
last_names = "Gates Joy Richie Jobs Ellison".split()

full_names = zip(first_names, last_names)  # <3>
print("full_names:", full_names)
print()

for first_name, last_name in full_names:
    print("{} {}".format(first_name, last_name))

fn = zip(first_names, last_names)
print(list(fn))
print(list(fn))
print()

for i, color in enumerate(colors):
    print(i, color)
print()

print(list(enumerate(colors)))

e = enumerate(colors)
print(e)
# print(len(e))  NO LENGTH
