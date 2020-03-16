#!/usr/bin/env python

list1 = list()  # new, empty list

list2 = ['alpha', 'beta', 'gamma', 1, 5, 19, None, True, 8.7]

list3 = []

thing = "fee:fi:fo:fum"
list4 = thing.split(':')
print(list4)

# list5 = list(any-iterable-object)

places = ['Vancouver', 'Victoria', 'Whistler', 'Banff']

print(len(places))
print(places[0], places[2])
print(places[-1])  # places[len(places)-1]

places.append("Lake Louise")
places.append("Canmore")
print(places)

places.insert(0, 'Kananaskis')
places.insert(4, 'Jasper')
print(places)

more_places = ['Regina', 'Whitehorse', 'Calgary']

places.extend(more_places)
print(places)

places.insert(1000000, 'Hope')
print(places)

# places[100] = "wherever"  # NOT A THING!

del places[0]
print(places)

p = places.pop()
print(p)
print(places)

p = places.pop(2)
print(p)
print(places)

places.remove('Canmore')
print(places)

print(places[0], places[5], places[-1])

print(places[0:4])  # places[0], places[1], places[2], places[3]
print(places[3:6])
print(places[3:100])
print(places[3:])
print(places[:4])  # first 4
print(places[3:-1])

print(places[6:2:-1])  # start at 6 and count down
print(places[::2])  # every other element

actor = 'Chris Hemsworth'
print(actor[:5])
print(actor[-5:])
print(actor[6:9])

print(places, '\n')

for place in places:
    # place = next(places)
    print("Let's go to {}".format(place))
print()

for thing in [5, 8.9, "foo", True]:
    print(thing, type(thing))
print()





