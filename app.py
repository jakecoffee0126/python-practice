class Microwave:
    def __init__(self, brand, power):
        self.brand = brand
        self.power = power
        self.turned_on = False

    def turn_on(self):
        if self.turned_on:

            print(f"{self.brand} is already on")
        else:
            self.turned_on = True
            print(f"{self.brand} is on now")

    def turn_off(self):
        if self.turned_on:
            self.turned_on = False
            print(f"{self.brand} is off now")
        else:

            print(f"{self.brand} is already off")

    def run(self, time):
        if self.turned_on:
            print(f"{self.brand} is running for {time} seconds")
        else:
            print(f"Please turn on {self.brand} first")

    def __add__(self, other):
        return f"Combined power of {self.brand} and {other.brand} is {self.power + other.power}W"

    def __str__(self):
        return f"{self.brand} Microwave with {self.power}W power"


lg = Microwave("LG", 1000)
lg.turn_off()
lg.turn_off()
lg.run(10)
lg.turn_on()
lg.turn_on()

smg = Microwave("Samsung", 1200)
smg.turn_on()
smg.run(20)
smg.turn_off()

print(lg + smg)

print(lg)  # for __str__
