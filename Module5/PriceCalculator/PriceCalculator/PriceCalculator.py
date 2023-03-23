# Program Name: PriceCalculator
# Program Author: James Allen
# Class: Computer Programming ITSE 1302 7P1
# Description: This program calculates the price and totals of items
print("Welcome to Dollar Family!")
subTotal = 0
while True:  
    itemPrice = float(input("Enter item price: "))    
    if itemPrice == 0:
        break
    quantity = int(input("How many of item: "))
    firstTotal = itemPrice * quantity
    subTotal = firstTotal + subTotal
print("Subtotal: ${:.2f}".format(subTotal))
tax = subTotal * 0.0825
print("Tax: ${:.2f}".format(tax))
total = subTotal + tax
print("Total ${:.2f}".format(total))

