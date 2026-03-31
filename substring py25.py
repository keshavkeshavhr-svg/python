str="if you think you can or you can't, you are right"
print(str)
print(str.count("you"))#it counting number of string
str1="you"
print(str1 in str)# in this it checking the you is present in the str
print(str.index("you"))#it is indexing
print(str.find("you"))#both same
print(str.rindex("you"))#it counting from the right in the postive indexing rule is applying
print(str.rfind("you"))
print(str.find("python"))

#replaceing the substring
str="arju is dancing is"
print(str)
str1=str.replace("is","was")
print(str1)
print(str.startswith("arju"))
print(str.startswith("raju"))
print(str.endswith("dancing"))
print(str.endswith("singing"))
#packing and unpacking
str="rama"
print(str)
r1,r2,r3,r4=str
print(r1)
print(r4)