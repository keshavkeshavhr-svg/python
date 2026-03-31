class Bike:
    def __init__(self):
        self.brand="royal"
        self.model=1990
        self.color="black"
    def speed(self):
        print("royal is very speed")
        print(self.color)
        print(self)
b1=Bike()
print(b1.brand)
print(b1.model)
print(b1.color)
b1.speed()
print(b1)
