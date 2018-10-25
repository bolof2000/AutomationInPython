import math
from math import sqrt


class Car(object):

    def __init__(self):

        print("base class")

    def accelerate(self):
        print("evrry car accelerates")

    def stop(self):
        print("every class stops")


class BMW(Car):

    def __init__(self):

        Car.__init__(self)
        #initiaze the parent class in child class
        print("initializgin the child class")

    def fly(self):
        print("print ")

    def electric(self):
        print("electric car")


c = Car()
c.accelerate()
b = BMW()
b.fly()
b.accelerate()


class modulesTest():

    def squareroot(self):
        print(math.sqrt(100))

