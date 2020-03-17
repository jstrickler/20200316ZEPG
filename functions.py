#!/usr/bin/env python
import spam


def get_message():
    return "Hello, ZE world"


m = get_message()
print(m)


def say_message():
    m = get_message()
    print(m)


say_message()


def greet(whom="world"):
    print("Hello,", whom)

greet("world")
greet("Mom")
greet("Norbert")
greetee = "Kanye West"
greet(greetee)
greet()


def process_log(folder, *log_dates):
    print(folder)
    print(log_dates)


process_log('DATA', '20191218', '20191113', '20200128')
process_log('DATA', '20191218')
process_log('/home/jstrick')

spam.toast()
spam.wombat()


def barf(a, b, *c):
    pass












