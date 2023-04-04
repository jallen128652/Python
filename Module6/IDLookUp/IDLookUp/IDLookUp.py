# Program Name: IDLookUp
# Program Author: James Allen
# Class: Computer Programming ITSE 1302 7P1
# Description: This program searches a list and prints whether or not
# the input matches the id list

#idList stores all the IDs that have access to the archives
idList = ["18550", "98551", "78532", "18521", "48526", "38520", "88578", \
"98583", "48566", "28579", "18586", "88559", "18593", "38570", "28596", "58537", \
"58516", "18577", "78557", "18503", "98501", "28504", "98539"]

print("ID Search\n")
# while loop with setinel control for input searches
search = input("Enter an ID or XXX to quit: ")
while search != "XXX":
	if search in idList:
		print(str(search) + " is in the list.\n")
	else:
		print(str(search) + " is NOT in the list.\n")
	search = input("Enter an ID or XXX to quit: ")
if search == "XXX":
	print("Goodbye!")


