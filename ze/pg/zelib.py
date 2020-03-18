#!/usr/bin/env python
"""
Amazing module for my superb ZE students.

This module has blah blah utilities to make
everything better
"""

def main():
    """
    Program starting point
    """
    print("Hi, ZE students!")
    spam()


def spam():
    """
    Silly function for demo

    :return: None
    """
    print("Hello from spam!")
    _toast()


def ham():
    """
    Another silly function

    :return: None
    """
    print("Hello from ham!")


def _toast(): # pseudo-private
    """
    A *private* (sort of) silly function

    :return: None
    """
    print("  ...doing toasty things")


class Dog():
    """
    A class representing Man's best friend
    """
    def bark(self):
        """Make a canine noise"""
        print("Woof! Woof!")


COLORS = ['red', 'blue', 'purple', 'pink']

if __name__ == '__main__':
    main()
