# MichiganCities.py - This program prints a message for invalid cities in Michigan.  
# Input:  Interactive
# Output:  Error message or nothing

# Initialized list of cities
citiesInMichigan = ["Acme", "Albion", "Detroit", "Watervliet", "Coloma", "Saginaw", "Richland", "Glenn", "Midland", "Brooklyn"] 
#numCities = len(citiesInMichigan)
# Get user input
inCity = input("Enter name of city: ")

# Write your test statement here to see if there is a match.
if inCity in citiesInMichigan:
	print("City found.")
else:
	print("Not a city in Michigan")
# If the city is found, print "City found."

# Otherwise, "Not a city in Michigan" message should be printe
