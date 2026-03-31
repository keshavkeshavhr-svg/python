total=0
while True:
    price=float(input("enter the item prices (0 to stop): "))
    if price==0:
        break
    total=price+total
if total>5000:
    discount=total*0.2
elif total>2000:
    discount=total*0.1
else:
    discount=0
final_bill=total-discount
print("total amount:",total)
print("discount:",discount)
print("final_bill:",final_bill)


