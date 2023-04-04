# Program Name: Patrons
# Program Author: James Allen
# Class: Computer Programming ITSE 1302 7P1
# Description: This program populates a parrallel list of patrons per 
# month and then calculates the low, high and average.

# declare lists and variables
months = ["January", "February", "March", "April", "May", "June", 
		  "July", "August", "September", "October", "November", "December"]
patrons = []
x = len(months)
minPatrons = 999
maxPatrons = -1
total = 0
# loop input for patrons list
for x in range (0, 12):
	num = float(input("Enter number of patrons for " + str(months[x]) + ": "))
	patrons.append(num)
	# determin highest and lowest patron month
	if num > maxPatrons:
		maxPatrons = num
		maxMonth =months[x]
	if num < minPatrons:
		minPatrons = num
		minMonth =months[x]
	# total up number of patrons (accumulator)
	total += num
print(maxMonth + " hand the most patrons.")
print(minMonth + " hand the least patrons.")
print("Average monthly visitors are " + str(total / 12))

