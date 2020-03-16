#!/usr/bin/env python

print('26\u00B0')  # <1>
print('26\N{DEGREE SIGN}')  # <2>
print(r'26\u00B0\n')  # <3>
print()

print('we spent \u20ac1.23M for an original C\u00e9zanne') # <4>
print("Romance in F\u266F Major")
print()

data = ['\U0001F95A', '\U0001F414'] # <5>
print(sorted(data))

actor = "Chris Hemsworth"
print(len(actor), actor.upper())  # Python has both!

print(actor, actor.upper(), actor.lower())
print(actor.count('h'))
print(actor.lower().count('h'))
print(actor.startswith('Chris'), actor.startswith('Liam'))
print("swo" in actor, "sow" in actor)

s = "     All my exes live in Texas     "
print("|" + s.lstrip() + "|")  #  ' \t\n\r\b\f'
print("|" + s.rstrip() + "|")
print("|" + s.strip() + "|")
print()


s = "xyxxyyxxxyyyAll my exes live in Texasyxyxyyyyyyyyyxxxxx"
print("|" + s.lstrip('xy') + "|")
print("|" + s.rstrip('xy') + "|")
print("|" + s.strip('xy') + "|")
print()

thing_list = 'beaver;moose;maple leaf;pine marten'

items = thing_list.split(';')
print(items)

place_list = 'Vancouver Calgary Regina'
places = place_list.split()
print(places)

