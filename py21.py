total=0
for i in range(1,6):
    marks=int(input("enter marks for subject"+str(i)+":"))
    total=total+marks
average=total/5
print("total marks:",total)
print("average:",average)
if average>=90:
    print("grade: A")
elif average>=75:
    print("grade: B")
elif average>=50:
    print("grade: C")
else:
    print("grade: fail")

