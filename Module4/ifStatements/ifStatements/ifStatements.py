"""
HouseSign.py - This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
    # Charge for this sign.
    # Number of characters.
    # Color of characters.
    # Type of wood.

charge = 0.0
baseCharge = 35.0
numChars = 8
charCharge = 0
color = "gold"
woodType = "oak"

# Write assignment and if statements here as appropriate.

if numChars > 5:
    charge = (numChars - 5) * 4 + baseCharge
else:
    charge = 0 + baseCharge
if woodType == "oak":
    charge = charge + 20.0
if color == "gold":
    charge = charge + 15.0

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
