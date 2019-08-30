#!/usr/bin/env python

def generator(limit):
    i = 0
    while i < limit:
        i += 1
        yield i

def main():
    for x in generator(10):
        print(x)

main()