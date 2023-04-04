# JumpinJava.py - This program looks up and prints the names and prices of coffee orders.  
# Input:  Interactive
# Output:  Name and price of coffee orders or error message if add-in is not found 

# Declare variables.
NUM_ITEMS = 5 # Named constant

# Initialized list of add-ins
addIns = ["Cream", "Cinnamon", "Chocolate", "Amaretto", "Whiskey"]

# Initialized list of add-in prices
addInPrices = [.89, .25, .59, 1.50, 1.75]
orderTotal = 2.00  # All orders start with a 2.00 charge
# Get user input
addIn = input("Enter coffee add-in or XXX to quit: ")

# Write the rest of the program here.
while addIn != "XXX":
	foundIt = False
	for x in range(NUM_ITEMS):
		if addIn in addIns[x]:
			foundIt = True
			print(addIns[x] + " Price is $" + str(addInPrices[x]))			
			orderTotal = orderTotal + addInPrices[x]
			break
	if not foundIt:
			print("Sorry we do not carry that.")
		
	addIn = input("Enter coffee add-in or XXX to quit: ")
	
print("Order Total is $" + str(orderTotal))
