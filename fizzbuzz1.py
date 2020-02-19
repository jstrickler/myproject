#!/usr/bin/env python

LIMIT = 50 + 1

def main():
    fb(LIMIT)


def fb(limit):
    for i in range(1, limit):
        div_by_3 = not i % 3
        div_by_5 = not i % 5
        if div_by_3:
            print("FIZZ", end='')
        if div_by_5:
            print("BUZZ", end='')
        if not any([div_by_3, div_by_5]):
            print(i, end='')
        print(", ", end='')
    print()

if __name__ == '__main__':
    main()
