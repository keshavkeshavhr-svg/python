
print("WELCOME TO OUR SHOP")
print("1.t-shirts")
print("2.pant")
print("3.shirt")
print("4.children dress")
amount=(100,200,300,400)
option=int(input("please select your choice"))
if option==1:
    print("your selcted item is t-shirts")
    amount = int(input("please pay the bill"))
    if amount==100:
        print("payment is secessfull,visit agin")
    elif option==2:
        print("your selected item is pant")
        amount = int(input("please pay the bill"))
        if amount==200:
                print("payment is secessfull,visit agin")
        elif option==3:
            print("your selected item is shirt")
            amount = int(input("please pay the bill"))
        elif option==4:
            print("your selected item is children dress")
        else:
            print("please pay the vaild amount")
    else:
        print("please pay the vaild amount")
else:
    print("please select the crt option")


