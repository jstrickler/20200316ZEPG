#!/usr/bin/env python

s1 = "spam\n"
s2 = 'spam\n'
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r'spam\n'

print(s1)
print(s2)
print(s5)
print("Guido's the BDFL of Python")
print('Guido is the "BDFL" of Python')
print('Guido\'s the BDFL of Python')  # not pythonic

print("""Guido's the "BDF" of Python""")

