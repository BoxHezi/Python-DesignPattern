#!/usr/bin/env python

class CPU:
    def freeze(self):
        print("Freezing processor")

    def jump(self, position):
        print("Jumping to: %s" % position)

    def execute(self):
        print("Excuting")

class Memory:
    def load(self, position, data):
        print("Loading from {0} data: '{1}'.".format(position, data))

class SolidStateDrive:
    def read(self, lba, size):
        print("Some data from sector {0} with size {1}".format(lba, size))

class ComputerFacade:
    def __init__(self):
        self.cpu = CPU()
        self.memory = Memory()
        self.ssd = SolidStateDrive()

    def start(self):
        self.cpu.freeze()
        self.memory.load("0x00", self.ssd.read("100", "1024"))
        self.cpu.jump("0x00")
        self.cpu.execute()

def main():
    """
    >>> computer_facade = ComputerFacade()
    >>> computer_facade.start()
    Freezing processor
    Loading from 0x00 data: 'Some data from sector 100 with size 1024.'
    Jumping to: 0x00
    Excuting
    """

if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.ELLIPSIS)