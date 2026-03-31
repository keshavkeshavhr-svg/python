class Mobile:
    def __init__(self):
        self.brand="nokia"
    def call(self):
        print("mobile is calling")
    @staticmethod
    def charge():
        print("mobile is chargeing")
    @classmethod
    def hang(cls):
        print("mobile is hanging")
m1=Mobile()
print(m1.brand)
m1.call()
m1.charge()
m1.hang()#it is not a standerd way of call static and class
Mobile.charge()
Mobile.hang()