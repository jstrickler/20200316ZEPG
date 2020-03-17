#!/usr/bin/env python

class1 = ['Ralph', 'Betty', 'Marty', 'Jessica', 'Saurabh']

class2 = ['Carlo', 'Anitha', 'Dzmitry', 'Betty',
          'Ralph', 'Josue']

c1 = set(class1)
c2 = set(class2)

print("both:", c1 & c2)
print("just one:", c1 ^ c2)
print("all:", c1 | c2)
print("just c1:", c1 - c2)
print("just c2:", c2 - c1)
c1 = c1 - c2  # remove items in c2 from c1
print("c1 after subtraction:", c1)

cities = ['Calgary', 'Vancouver', 'Calgary', 'Vancouver',
          'Calgary', 'Vancouver', 'Calgary', 'Vancouver', 'Calgary', 'Vancouver', 'Calgary', 'Vancouver', 'Calgary', 'Vancouver', 'Edmonton', 'Ottawa', 'Kitchener', 'Toronto', 'Calgary', 'Vancouver',
          'Calgary', 'Vancouver', 'Calgary', 'Vancouver']

ucities = set(cities)
print(ucities)

