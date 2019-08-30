#!/usr/bin/env python3

class Singleton:
    # instance stored
    __instance = None

    @staticmethod
    def getInstance():
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        if Singleton.__instance != None:
            raise Exception("Instance exist already!")
        else:
            Singleton.__instance = self

a = Singleton()
# b = Singleton()
c = Singleton.getInstance()
d = Singleton.getInstance()

print(a)
print(c)
print(d)