#!/usr/bin/env python

file_name = 'DATA/octopus.txt'
try:
    with open(file_name) as file_in:
        pass
except FileNotFoundError as err:
    print(err)

colors = ['red', 'green', 'mauve', 'taupe', 'ecru']
try:
    print(colors[8])
except IndexError as err:
    print(err)

for n in 5.6, 8.1, 3.4, 'abc', 0.0, 7.6, 9.9, 2.7:
    try:
        result = 23 / n
    except ZeroDivisionError as err:
        print(err, type(err))
    except (TypeError, ValueError) as err:
        print(err, type(err))
    except Exception as err:
        print("Wow!", err, type(err))
    else:
        print(result)
    finally:
        pass

