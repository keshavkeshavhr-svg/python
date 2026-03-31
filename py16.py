correct_pin=1234
import time
bal=10000
print("WELCOME TO ATM")
card=int(input("please insert the card 1.yes 2.no"))
if card==1:
    print("please slect the lang")
    lang=int(input("1.kannada 2.english "))
    if lang==1:
        print("please select english")
    elif lang==2:
        print("your selected lang is english")
        pin=int(input("please enter the pin"))
        if pin==1234:
            print("pin is verified successfully")
            option=int(input("1.check balance 2.withdraw"))
            if option==1:
                print(f"checking balance{bal}")
            elif option==2:

                withdraw=int(input("please enter the amount"))
                if (withdraw<=bal):

                    if withdraw%100==0:
                        print("amount is processing")
                        time.sleep(5)
                        bal-=withdraw
                        print("amount is withdrawn")
                        print("thank you sir,visit again")
                    else:
                        print("enter the amount in 100s")
                else:
                    print("insuffient balance")
        else:
            print("wrong pin")

    else:
        print("please select english")

else:
    print("please insert card properly")
