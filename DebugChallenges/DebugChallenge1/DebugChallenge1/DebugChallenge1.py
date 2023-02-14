#The following program accepts the price of an
#item as input, and then calculates the total price after adding
#city and state sales tax.  The state tax rate is 6%
#and the city tax rate is 2%.  There are five bugs/errors in this program.

STATE_TAX_RATE = 0.06
CITY_TAX_RATE = 0.02
itemPrice = float(input("Enter price: "))

totalTax = (itemPrice * STATE_TAX_RATE) + (itemPrice * CITY_TAX_RATE)

totalPrice = itemPrice + totalTax

print("Item price is " + str(itemPrice) + " and total tax is " + str(totalTax))
print("Total price is " + str(totalPrice))
