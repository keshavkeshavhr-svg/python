def outer():
    a=100
    b=200#nonnlocal varibales it is only in the nested functions
    print(a)
    print(b)
    def inner():
        nonlocal a
        a=300
        b=400# this are the local varibales
        print(a)
        print(b)
    print(a)
    inner()
    print(a)
outer()
#nested
def outer():
    a=10
    b=20
    print(a)
    print(b)
    def inner():
        c=15
        print(a)
        print(c)
    inner()
outer()
#
def outer():
    a=100
    print(a)
    print(b)
    def inner():
        b=200
        print(b)
    inner()
outer()