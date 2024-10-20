price=int(input())
qty=int(input())
amount=price*qty
if amount>10000:
    print ("10% discount applicable")
    discount=amount*10/100
    amount=amount-discount
elif amount>5000:
    print("5% discont is applicable")
    discount = amount*5/100
    amount = amount-discount
elif amount>2000:
    print("2% discount is applicable")
    discount = amount*2/100
    amount = amount-discount
elif amount > 1000:
    print("1% discount is applicable")
    discount = amount*1/100
    amount =  amount - discount
else:
    print("No discount is applicable")
print("amount payable:",amount)