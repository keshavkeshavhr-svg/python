'''class OS:
    def __init__(self):
        self.status=True
        print("os is ready")
    def getOS(self):
        print("os is installing")
class Mobile:
    def __init__(self,name):
        self.mname=name
        self.o=OS()
        print("moblie is ready")
        print("with os installed")
m1=Mobile("apple")
print(m1.mname)
print(m1.o.status)
m1.o.getOS()
"""del m1
print(m1.o.status)""" '''

#aggregate
class Charger:
    def __init__(self,name):
        self.cname=name
    def getCharger(self):
        print("chager is working")
class Mobile:
    def __init__(self,name):
        self.mname=name
        selfc=""
    def hasMobile(self,p):
        self.c=p
m1=Mobile("IQ")
c1=Charger("c pin")
m1.hasMobile(c1)
print(m1.mname)
print(m1.c.cname)
m1.c.getCharger()
del m1
print(c1.cname)
c1.getCharger()


