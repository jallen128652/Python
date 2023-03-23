# Program Name: CustomCanvases
# Program Author: James Allen
# Class: Computer Programming ITSE 1302 7P1
# Description: This program calculates cost for canvases orders
numCanvas = int(input("Enter number of canvases: "))
totalSF = 0
count = 1
while count <= numCanvas:
	length = int(input("Enter canvas " + str(count) + " length (ft): "))
	width = int(input("Enter canvas " + str(count) + " width (ft): "))
	sqft = length * width
	count += 1
	totalSF += sqft	
if totalSF < 20:
	print("Order not big enough.")
else:
	print("Price per sq foot: $4.99")
	print("Total canvas square feet: {:.1f}".format(totalSF))
	totalPrice = totalSF * 4.99
	print("Total Price: ${:.2f}".format(totalPrice))