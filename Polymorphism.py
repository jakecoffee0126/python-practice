# Polymorphism
# https://www.w3schools.com/python/python_polymorphism.asp

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("sail")


class Plane(Vehicle):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("fly")


car1 = Car("Volve", "cx-5")
boat1 = Boat("Ibiza", "Touring20")
plane1 = Plane("Boeing", "747")

for x in (car1, boat1, plane1):
    # x.move()

    print(f'Brand: {x.brand} and Model: {x.model}')
    x.move()
