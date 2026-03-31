class Car:
    def __init__(self):
        self.name="BMW"
        self.age=4
        self.color="black"
    def speed(self):
        print("BMW is good in speed")
    def petrol(self):
        print("BMW is petrol engine")
c1=Car()
print(c1.name)
print(c1.age)
print(c1.color)
c1.speed()
c1.petrol()