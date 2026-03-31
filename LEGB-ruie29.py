a=20
def outer():
    a=10
    def inner():
        a=15
        print(a)
    inner()
outer()
#
a=20
def outer():
    #a=10
    def inner():
        #a=15
        print(a)
    inner()
outer()
#
from math import pi
#pi=20
def outer():
    #pi=10
    def inner():
        #pi=15
        print(pi)
    inner()
outer()
#closure
def outer():
   print("inside outer")
   def inner():
       print("inside inner")
   return inner
ref=outer()
ref()

