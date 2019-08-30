#!/usr/bin/env python

class SalesManager:
    def talk(self):
        print("Sales Manager ready to talk")

class Proxy:
    def __init__(self):
        self.busy = "No"
        self.sales = None

    def talk(self):
        # print("Proxy checking for Sales Manager Availability")
        if self.busy == "No":
            self.sales = SalesManager()
            self.sales.talk()
        else:
            print("Sales manager is busy")

class NoTalkProxy(Proxy):
    def talk(self):
        # print("Proxy checking for Sales Manager availability")
        print("This sales manager won't talke to you")

if __name__ == "__main__":
    p = Proxy()
    p.talk()
    p.busy = "Yes"
    p.talk()
    p = NoTalkProxy()
    p.talk()
    p.busy = "Yes"
    p.talk()