try:
    a=int(input("enter the value "))
    b=int(input("enter the value"))
    res=a/b
    print(res)
except Exception as e:
    print(e.__str__())
else:
    print("pgm run successfully")