#!/usr/bin/env python

person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

print(person, len(person))
print(person[0])

print(person[0], person[1])

first_name, last_name, product, dob = person

#  list-of-variables = iterable-object


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

print(people[0], '\n')
print(people[0][0], '\n')
print(people[0][0][0], '\n')

for p in people:
    # p = next(people)
    print(p)
print('-' * 60)

for p in people:
    first_name, last_name, product, dob = p
    print(first_name, last_name)
print('-' * 60)

for first_name, last_name, product, dob in people:
    # first_name, last_name, product, dob = next(people)
    print(first_name, last_name)
print('-' * 60)

items = [
    ['a', 5, 'pamplemousse', 'wombat'],
    ['b', 8],
    ['m', 16],
    ['e', 2, 25]
]

for letter, number, *extra in items:
    print(letter * number, extra)
print()
