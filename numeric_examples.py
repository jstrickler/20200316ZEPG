#!/usr/bin/env python

i1 = 100
i2 = 0x100
i3 = 0b100
i4 = 0o100

print(i1, i2, i3, i4)

f1 = 123.456
f2 = 123.
f3 = .456
f4 = 1.2343e33

print(1/3)
print(17/7)
print()

x = 23
y = 7

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x // y)  # 3.5 rounded to 3, -3.5 rounded to -4
print(x ** y)  # raise to power (exponentiation)
print(x % y)  # modulo (remainder after division)

x = 5
x += 3  # x = x + 3
x /= 2  # x = x / 2
x *= 10  # x = x * 10
print(x)

# Python does NOT support x++ or ++x  (or x-- or --x)
x = 23
y = 7

print(divmod(x, y))

a = 123
b = "123"

print(a * 3)
print(b * 3)
print(int(b) * 3)

x = "    7654    "
print(int(x) * 10)

d = "DeadBeef"
# print(int(d))  # FAIL!

print(int(d, 16))

b = "1001001001"
print(int(b, 2))

s = "100"
print(int(s, 10), int(s, 2), int(s, 16), int(s, 31))









