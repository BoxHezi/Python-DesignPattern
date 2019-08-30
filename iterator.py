#!/usr/bin/env python

class RandomIterator:
    __limit = None
    current_num = 0

    def __init__(self, limit):
        self.__limit = limit

    def __iter__(self):
        return self
    
    def __next__(self):
        i = self.current_num
        if i > self.__limit:
            raise StopIteration
        
        self.current_num += 1
        return i

def main():
    r = RandomIterator(10)
    for i in r:
        print(i)

if __name__ == "__main__":
    main()