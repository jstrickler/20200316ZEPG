#!/usr/bin/env python

value = 56

if value > 75:
    print("wallaby")
    print("dingo")
elif value > 50:  # else if
    print("kangaroo")
    print("platypus")
# elif value == True:  # is value equal to 1??
#     print("Not gonna happen")
else:
    print("wombat")
    print("kookaburra")

print("Done")

#  A?B:C  ternary operator

#  B if A else C

color = "red" if value > 50 else "blue"

print("color is", color)

#  == != > < >= <=

if value <= 56:
    print("Wombats!!")

if value == "Porky Pig":
    print("that's all folks")

if not value > 10:
    print("huh?")

# === operator

junk1 = [1, 2, 3]
junk2 = junk1
junk3 = [1, 2, 3]

print(junk1 == junk2, junk1 is junk2)
print(junk1 == junk3, junk1 is junk3)

#  and  or  not

#  X and Y
#  X or Y
#  not X

#  func1() and func2()

w = 0
x = 5
y = 10
print(x and y)
print(y and x)
print(w and y)









