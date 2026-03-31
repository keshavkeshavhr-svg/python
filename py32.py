"""def fun1():
    print("inside fun1 in f2")
def fun2():
    print("insude fun2 in f2")"""





"""l2=[]
l1=input("enter five numbers ").split()
for i in l1:
    i=int(i)
    l2.append(i)
print(l1)

print(l2)"""


L=[]
for i in range(0,6):
    num=int(input("Enter a number: "))
    L.insert(i,num)
print(L)

i=0
while i <= 4:
    num = int(input("enter a num"))
    L.insert(i, num)
    i = i + 1
print(L)