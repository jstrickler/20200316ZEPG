#!/usr/bin/env python

i = 0
while i < 5:
    print(i)
    i += 1
print()

# NOT for(i = 0; i < X; i++) { }

while True:
    file_to_delete = input("Enter file name (or q to quit): ")
    if file_to_delete == 'q':
        break  # exit loop NOW
    if file_to_delete == '':
        continue  # go to top of loop

    print("Deleting", file_to_delete)

