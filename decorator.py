#!/usr/bin/env python

def outer(func):

    def inner():
        print("Before func is called")
        func()
        print("After func is called")
    
    # print("Inner: " + str(inner()))
    return inner

@outer
def print_inner_func():
    print("Inner function")

# outer = outer(print_inner_func)
# outer()

print_inner_func()