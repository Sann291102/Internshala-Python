## using conditions statements to calculate the price of objects
price = int(input('Enter the price of your pen:'))
quantity = int(input("How many pens are required :"))
amount = price*quantity
if amount>100:
    print("Woah you're eligible for 10 percent discount on this order.")
    discount = amount*10/100
    amount = amount-discount
else:
    print("woops! No dicount is applicable.")
print("The required amount to be paid is RS:", amount)
