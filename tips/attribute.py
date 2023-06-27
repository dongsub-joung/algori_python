class Person:
    def __init__(self):
        self.whatever= "hi"
        self.TEN= 10

    def greeting(self):
        print(self.whatever*self.TEN)

dongsub= Person()
dongsub.greeting()