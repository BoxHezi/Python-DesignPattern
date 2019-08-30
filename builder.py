#!/usr/bin/env python

class Director:
    __builder = None

    def setBuilder(self, builder):
        self.__builder = builder

    def getCar(self):
        car = Car()

        body = self.__builder.getBody()
        car.setBody(body)

        engine = self.__builder.getEngine()
        car.setEngine(engine)
        
        i = 0
        while i < 4:
            wheel = self.__builder.getWheel()
            car.attachWheel(wheel)
            i += 1

        return car

class Car:
    def __init__(self):
        self.__wheels = list()
        self.__engine = None
        self.__body = None

    def setBody(self, body):
        self.__body = body
    
    def setEngine(self, engine):
        self.__engine = engine
    
    def attachWheel(self, wheel):
        self.__wheels.append(wheel)

    def specification(self):
        print("Body: %s" % self.__body.shape)
        print("Engine: %s" % self.__engine.horsepower)
        print("Tire Size: %d\'" % self.__wheels[0].size)
    
class Builder:
    def getWheel(self):
        pass
    
    def getEngine(self):
        pass
    
    def getBody(self):
        pass

class jeepBuilderBuilder(Builder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 22
        return wheel

    def getEngine(self):
        engine = Engine()
        engine.horsepower = 400
        return engine

    def getBody(self):
        body = Body()
        body.shape = "SUV"
        return body

class NissanBuilder(Builder):
    def getWheel(self):
        wheel = Wheel()
        wheel.size = 16
        return wheel
    
    def getEngine(self):
        engine = Engine()
        engine.horsepower = 200
        return engine
    
    def getBody(self):
        body = Body()
        body.shape = "sport"
        return body
    
class Wheel:
    size = None

class Engine:
    horsepower = None

class Body:
    shape = None

def main():
    jeepBuilder = jeepBuilderBuilder()
    nissianBuilder = NissanBuilder()

    director = Director()

    print("Jeep")
    director.setBuilder(jeepBuilder)
    jeep = director.getCar()
    jeep.specification()

    print("Nissan")
    director.setBuilder(nissianBuilder)
    nissan = director.getCar()
    nissan.specification()


if __name__ == "__main__":
    main()