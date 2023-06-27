class Person:
    def moving(self):
        print("moving")
    def eating(self):
        print("eating")

dongsub= Person()
dongsub.eating()
print(isinstance(dongsub, Person))