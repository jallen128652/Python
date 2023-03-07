"""
Airline.py - This program determines if an airline passenger is
eligible for a 25% discount.
"""

# Passenger's name.
passengerName = input("Enter passenger's name: ")
# String version of passenger's age.
ageString = input("Enter passenger's age: ")
# Passenger's age.
passengerAge = int(ageString)

# Test to see if this customer is eligible for a 25% discount.
if passengerAge <= 6 or passengerAge >= 65:
    print("Customer Name: " + passengerName)
    print("Customer Age : " + str(ageString))
    print("Passenger is eligible for a discount.")
else:
    print("Customer Name: " + passengerName)
    print("Customer Age : " + str(ageString))
    print("Passenger is not eligible for a discount.")
