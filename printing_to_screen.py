#!/usr/bin/env python

actor = "Chris Hemsworth"
city = "Sidney"

value = 23 / 13

print(actor)  # like  print(str(actor) + "\n")
print(actor, city)

print(actor, city, sep='/')
print(actor, city, sep=' and ')

print(actor)
print(city)

print(actor, end=' ')
print(city)

print(actor, "lives in", city)

#       0           1       0      1
print("%s lives in %s" % (actor, city))

#       0           1          0       1
print("{} lives in {}".format(actor, city))  # modern formatting

print("{1} lives in {0}".format(actor, city))  # modern formatting

foo = 25

print("foo is {}".format(foo))

print(value)

print("value is {:.2f}".format(value))

print("foo is {:08d}".format(foo))
print("foo is {:8d}".format(foo))

big_num = 23094203984209348209384203
print("big number is {:,d}".format(big_num))

print(f"{actor} lives in {city}")
print(f"value is {value:8.2f}")



