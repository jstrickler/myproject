#!/usr/bin/env python

print('26\u00B0')  # <1>
print('26\N{DEGREE SIGN}')  # <2>
print(r'26\u00B0\n')  # <3>
print()

print('we spent \u20ac1.23M for an original C\u00e9zanne') # <4>
print("Romance in F\u266F Major")
print()

data = ['\U0001F95A', '\U0001F414'] # <5>
print(sorted(data), '\n')

print("\U0001F92F" * 30, '\n')

# Mahjong Tiles Range	U+1F000..U+1F02F

for i in range(0x1F000, 0x1F02F + 1):
    print(chr(i), end=' ')
print("\n")

