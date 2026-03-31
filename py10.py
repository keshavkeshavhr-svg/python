a=int(input("Enter a num"))
b=int(input("Enter a num"))
c=int(input("Enter a num"))
if a>b and a>c:
    print("a is greater than b")
elif b>a and b>c:
    print("b is greater than a")
elif c>a and c>b:
    print("c is greater")
else:
    print("all are equal")
