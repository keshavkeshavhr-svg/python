try:
    a=int(input("enter the value"))
    b=(input ("enter the value"))
    res=a/b
    print(res)
except (ValueError) as e:
    print("it is value error")
except ZeroDivisionError as e:
    print("its zerodivisionerror")
except Exception as e:
    print("error occured")


