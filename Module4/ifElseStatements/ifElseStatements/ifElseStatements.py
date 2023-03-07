# LargeSmall.py - This program calculates the largest and smallest of three integer values. 
# Declare and initialize variables here
largest = None
smallest = None
num1 = 0
num2 = 0
num3 = 0
# Prompt the user to enter 3 integer values
print("enter 3 integer values")
num1 = int(input())
num2 = int(input())
num3 = int(input())

# Write assignments, and necessary if else statements here as appropriate


if int(num1) > int(num2) and int(num1) > int(num3):
	largest = int(num1)
else: 
	if int(num2) > int(num1) and int(num2) > int(num3):
		largest = int(num2)
	else: largest = int(num3)

if int(num1) < int(num2) and int(num1) < int(num3):
	smallest = num1
else: 
	if int(num2) < int(num1) and int(num2) < int(num3):
		smallest = num2
	else: smallest = int(num3)
# Output largest and smallest number. 
print("The largest value is " + str(largest))
print("The smallest value is " + str(smallest))
