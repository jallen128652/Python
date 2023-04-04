# Program Name: Cities
# Program Author: James Allen
# Class: Computer Programming ITSE 1302 7P1
# Description: This program populates a list a sorts descending
# declare list
city = []
# loop populating the list with setinel control
name = input("Enter City Name: ")
while name != "XXX":
	city.append(name)
	name = input("Enter City Name: ")
# sort the list descending
city.sort(reverse=True)
print("Sorted Cities (descending): ")
# print list elements individually
for x in city:
	print(x)