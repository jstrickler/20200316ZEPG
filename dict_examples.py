#!/usr/bin/env python

d1 = dict()
d2 = {'Jan': 31, 'Feb': 28, 'Mar': 31}
d3 = {}
d4 = dict(Jan=31, Feb=28, Mar=31)
months = ['Jan', 'Feb', 'Mar']
lengths = [31, 28, 31]
d5 = dict(zip(months, lengths))

print(d1)
print(d5)

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}
print(airports['YCC'])
print(airports['EWR'])
airports['YVR'] = 'Vancouver'
print(airports)

print(airports.get('YEG'))
print(airports.get('YEG', 'not found'))

del airports['YOW']
print(airports)

for abbr in ['RDU', 'LAX', 'YVR', 'OOT', 'BMZ']:
    print(abbr, abbr in airports)
print()

for abbr, name in airports.items():
    print(abbr, name)
print()

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

def by_value(item):
    return item[1], item[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()

print(airports.keys())
print(airports.values())

print(len(airports))









