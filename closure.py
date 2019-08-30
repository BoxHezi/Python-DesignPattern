#!/usr/bin/env python

def outer(msg):
    msg = msg

    def inner():
        print(msg)

    return inner

if __name__ == "__main__":
    outer("Hello World")