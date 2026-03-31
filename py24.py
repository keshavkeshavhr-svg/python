str=input("enter the string")
print(str)
if str.isalpha():
    print("str contains alpha")
elif str.isdigit():
    print("str contians only digits")
elif str.isalnum():
    print("contians both")
else:
    print("containing other charcter")
str=input("enter the string")
print(str)
str1=str.upper()
print(str1)
str2=str.lower()
print(str2)
str3=str.swapcase()
print(str3)
str=input("enter the sentence")
rev=""
str1=str.split()
for i in str1:
    #rev=i+rev
     rev=i+" "+rev
print(rev)