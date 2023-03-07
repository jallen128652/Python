#Program: Generations
#Course: ITSE 1302 7P1
#Author: James Allen
#Description: This program groups individuals by generational cohort

#declare variables
age = 0

#inputs
age = int(input("Enter the persons age: "))

#control structures
if age < 6:
	print("This person is from Generation Alpha")
elif age <= 24:
	print("This person is from Generation Z")
elif age <= 40:
	print("This person is from the Millenial Generation")
elif age <= 56:
	print("This person is from Generation X")
elif age <= 75:
	print("This person is a Baby Boomer")
elif age <= 93:
	print("This person is from the Silent Generation")
else: 
	print("This person is from The Greatest Generation")