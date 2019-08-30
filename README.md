# Design Pattern

## *Singleton* Pattern
* This pattern restricts the instantiation of a class to one object
* It is a type of creational pattern and involves only one class to create methods and specified objects
* It provides a global point of access to the instance created

## *Factory Method* Pattern
* In factory pattern, objects are created without exposing the logic to client and referring to the newly created object using a common interface
* Factory paterns are implemented in Pythonusing factory method

## *Builder* Pattern
* Builder Pattern is a unique design pattern which helps in building complex object using simple objects and uses an algorithmic approach
* In this design pattern, a builder class builds the final object in step-by-step procedure. This builder is independent of other objects

## *Facade* Pattern 
* Facade design pattern provides a unified interface to a set of interfaces in a subsystem. It defines a higher-level interface that any subsystem can use.
* A facade class knows which subsystem is responsible for a request

## *Adapter* Pattern
* Adapter pattern works as a bridge between two incompatible interfaces.
* This pattern involves a single class, which is responsible to join functionalities of independent or incompatible interfaces
* The adapter design pattern helps to work classes together. It converts the interface of a class into another interface based on requirement

## *Proxy* Pattern
* The proxy design pattern includes a new object, which is called "Proxy" in place of an existing object which is called the "Real Subject"
* The proxy object created the real subject must be on the same interface in such a way that the client should not get any idea that proxy is used in place of the read object
* Requests generated by the client to the proxy are passed through the real subject

## *Iterator*
* An iterator is an object adhering to the iterator protocol
  * basically this means that is has a next method, which, when called, returns the next item in the sequence, and
  * when there's nothing to return, raises the StopIteration exception

## *Generator*
* A generator is a function containing the keyword yield
* It must be noted that the mere presence of this keyword completely changes the nature of the function
  * this yield statement doesn't have to be invoked, or even reachable, but causes the function to be marked as a generator

## *Closures*
* A function closure is a combination of a function and a set of references to the variables in the scope in which the function was defined
* The latter is sometimes referred to as a referencing environment. This allows the function to be executed outside of where it is defined
* In Python, the referencing environment is stored as a tuple of cells. You can access them by using the func_closure or \_\_closure\_\_ attributes

## *Decorator*
* A decorator is a design pattern in which a class or function alters or adds to the functionality of another class or functions without using inheritance, or directly modifying the source code
* In Python, decorators are, in simplest terms, functions (or any callable objects) that take as input a set of optional arguments and a function or class, and return a function or class
https://www.geeksforgeeks.org/decorators-in-python/