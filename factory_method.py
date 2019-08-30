#!/usr/bin/env python

class Cup:
    color = ""

    @staticmethod
    def getCup(cupColor):
        if cupColor == "red":
            return RedCup()
        elif cupColor == "blue":
            return BlueCup()
        else:
            return None
    
class RedCup(Cup):
    color = "red"

class BlueCup(Cup):
    color = "blue"

red = Cup.getCup("red")
blue = Cup.getCup("blue")

print(red.__class__.__name__)
print(red.color)
print(blue.__class__.__name__)
print(blue.color)