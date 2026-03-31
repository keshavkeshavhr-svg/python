class Book:
    def __init__(self,page):
        self.__pages=page
    def setter(self,value):
        if value>0:
            self.__pages=value
    def getter(self):
        return self.__pages
b1=Book(100)
res1=b1.getter()
print(res1)
b1.setter(200)
res2=b1.getter()
print(res2)
b1.setter(-99)
res3=b1.getter()
print(res3)

#property en
class Person:
    def __init__(self):
        self.__name=""
    def getter(self):
        return self.__name
    def setter(self,value):
        self.__name=value
    getset=property(getter,setter)
p1=Person()
p1.getset="nidhi"
res=p1.getset
print(res)
#@decorater property
class Person:
    def __init__(self):
        self.__name=""
    @property
    def dataAccess(self):
        return self.__name
    @dataAccess.setter
    def dataAccess(self,value):
        self.__name=value
p1=Person()
p1.dataAccess="guru"
res=p1.dataAccess
print(res)

#public method into pravite method
class Dog:
    def __init__(self):
        self.breed="husky"
    def __bark(self):
        print("dog is barking")
    def helper(self):
        self.__bark()
d1=Dog()
d1.helper()

#
class Parent:
    def __init__(self):
        self.a=10
class child(Parent):
    def __init__(self):
        Parent.__init__(self)
        self.b=20
c1=child()
print(c1.b)
print(c1.a)
#
class A:#its only parent
    def __init__(self):
        self.a=100
class B(A):#its parent/child
    def __init__(self):
        #A.__init__(self)
        super().__init__()
        self.b=200
class C(B):#only child
    def __init__(self):
        #B.__init__(self)
        super().__init__()
        self.c=300
c1=C()
print(c1.c)
print(c1.b)
print(c1.a)
#
class Animal:
    def eat(self):
        print("animal is eating")
    def sleep(self):
        print("animal is sleeping")
    def hunt(self):
        print("animal is hunting")
class lion(Animal):
    pass
class tiger(Animal):
    pass
class fox(Animal):
    pass
l1=lion()
l1.eat()
l1.sleep()
l1.hunt()
t1=tiger()
t1.eat()
t1.sleep()
t1.hunt()
f1=fox()
f1.eat()
f1.sleep()
f1.hunt()
#
class A:
    def disp(self):
        print("inside a")
class B(A):
    def disp(self):
        print("inside b")
class C(B):
    def disp(self):
        print("inside c")
        B.disp(self)
        A.disp(self)
c1=C()
c1.disp()


