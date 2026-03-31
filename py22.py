str=" rahul is drinkig "
print(str)
str1=str.lstrip()
print(str1)
str2=str.rstrip()
print(str2)
str3=str.strip()
print(str3)
str=" r a j u"
print(str)
str1=""
for i in str:
    if i==" ":
        pass
    else:
        str1=str1+i
print(str1)
#
str=input("enter the string")
rev=""
for i in str:
        rev=i+rev
print(rev)
#
str="guru is drinking"
str1=str.split()
print(str)
print(str1)
#
str=input("enter the sentence")
rev=""
str1=str.split()
for i in str1:
    #rev=i+rev
     rev=i+" "+rev
print(rev)
#
str=input("enter the string")
rev=""
for i in str:
    rev=i+rev
print(rev)
if str==rev:
    print("palendrome")
else:
    print("not palendrome")