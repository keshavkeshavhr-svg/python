alpha=input("enter a alpha:")
a=ord(alpha)
print(a)
#number
num=int(input("enter the num:"))
b=chr(num)
print(b)
#neasted fuctions
def outer():
    print("inside outer")
    def inner():
        print("inside inner")
    inner()
outer()
#higher order function
def fun1():
    print("inside fun1")
def fun2(ptr):
    print("entering fun2")
    ptr()
    print("leaveing fun2")
fun1()
fun2(fun1)
#####
a=100
def fun1():
    global a
    a=10
    b=20
    print(a)
    print(b)
def fun2():
    global a
    a=15
    b=20
    print(a)
    print(b)
print(a)
fun1()
print(a)
fun2()
print(a)
#practice
x=5
def func():
    global x
    x=x+2
    func()
print(x)
#
a=4
if a%2:
    print("even")
else:
    print("odd")
#
word="developer"
x=word[ : :-2]
print(x)
#
food="pasta"
print(food.replace("a","n"))
#
food="keshav"
food.replace("k","j")#strings are immutable
print(a)



