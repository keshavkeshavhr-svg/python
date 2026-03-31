def add():
    a=20
    b=40
    c=a+b
    print(c)
add()
def fun1():
    print("inside the fun1")
def fun2():
    print("inside fun2")
a=fun1
b=fun2
a()
b()
#no parmaters and no return value
def add():
    a=12
    b=43
    c=a+b
    print(c)
add()
#with parmeters no return value
def add(a,b):
    c=a+b
    print(c)
x=69
y=12
add(x,y)
#no parmater with return value
def add(a,b):
    c=a+b
    return c
a=add(21,32)
print(a)
#with parmater and return value
def add(a,b):
    c=a+b
    return c
a=add(31,21)
print(a)
x=2
y=4
a=add(x,y)
print(a)
#condition statement
i=1
while i<=10:
    print(i*8)
    i=i+1
for i in range(1,11):
    print(i*8)
for i in range(1,11):
    print(i**2)





