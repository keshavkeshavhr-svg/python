
#
'''L=[]
i=0
while i<=4:
    num=int(input("enter a num"))
    L.insert(i,num)#in this we inserting value by useing indexing
    i=i+1
print(L)'''
#to write in vartical form
#by useing a for loop
"""i=0
while i<=4:
    print(L[i])
    i=i+1
#filtering
def even(num):
    if num%2==0:
        return True
    else:
        return False
L=[]
i=0
while i<=4:
    num=int(input("enter a num: "))
    L.insert(i,num)
    i=i+1
print(L)
i=0
while i<=4:
    data=L[i]
    chocie=even(data)
    if chocie==True:
        print(L[i])
    i=i+1"""

"""def even(num):
    if num%2==0:
        return True
    else:
        return False
L=[]
i=0
while i<=4:
    num=int(input("enter a num: "))
    L.insert(i,num)
    i=i+1
print(L)
res=list(filter(even,L))
print(res)"""

"""L=[]
i=0
while i<=4:
    num=int(input("enter a num: "))
    L.insert(i,num)
    i=i+1
print(L)
res=list(filter(lambda num:num%2==0,L))
print(res)"""

"""def generator():
    yield 1
    yield 2
    yield 3
res=generator()
print(res)
print(next(res))
print(next(res))
print(next(res))
print(next(res))"""
"""i=1
while i<=20:
    if i%2!=0:# is not even
        i+=1
        continue
    print(i)
    i=i+1
    if i>=20:
        break
print("try again")"""


pin=1234
trials=1
while trials<4:
    k=int(input(f"trail-{trials}| pin>>"))
    trials+=1
    if k==pin:
        print("correct")
        break
    else:
        print("incorrect")