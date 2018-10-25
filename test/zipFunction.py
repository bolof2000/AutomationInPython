

class Car():

    def __init__(self):

        print("default construtor")

    #define the functionalities of a car

    def drive(self):
        print("car drives")

    def stop(self):

        print("car stops")

    def accelerate(self):

        print("car accelerate")

#toyota inherits Car properties

class Toyota(Car):

    def __init__(self):

        Car.__init__(self)

    def fly(self):
        print("toyota flies")

    def zoom(self):
        print("toyota zoom")

    def drive(self):
        print("toyota drive in his own class")

c = Car()
t = Toyota()

c.accelerate()
c.drive()
t.accelerate()
t.fly()
t.drive()
