amount=(200,300,150)
print("WELCOME TO RESTAURANT")
import time
menu=int(input("This is our restaurent \n menu \n 1.pizza=200rs 2.burgur=300rs 3.mix rice=150rs"))
#2amount = (int(input("please pay the bill  sir/medam ")))
if menu==1:
    print("you order is pizza")
    time.sleep(3)
    print("take your order")
    amount = (int(input("please pay the bill  200rs sir/medam ")))
    if amount == 200:
        print("thank u sir")

elif menu==2:
    print("you order is burgur")
    time.sleep(3)
    print("take your order")
    amount = (int(input("please pay the bill sir/medam ")))
    if amount == 300:
        print("thank u sir")
elif menu==3:
    print("you order is mix rice")
    time.sleep(3)
    print("take your order")
    amount = (int(input("please pay the bill  sir/medam ")))
    if amount == 150:
        print("thank u sir")
    else:
        print("please pay the crt bill sir")
else:
    print("please order those items only")





