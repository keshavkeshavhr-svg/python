try:
    a=int(input("enter the value"))
    b=(input ("enter the value"))
    res=a/b
    print(res)
except (ValueError,ZeroDivisionError) as e:
    print("it is ve RO zde")
except Exception as e:
    print("error occured")