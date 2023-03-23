"""
MovieGuide.py

This program allows each theater patron to enter a value from
0 to 4 indicating the number of stars that the patron awards
to the Guide's featured movie of the week. The program
executes continuously until the theater manager enters a
negative number to quit. At the end of the program, the
average star rating for the movie is displayed.
"""

# Initialize variables.
totalStars = 0  # total of star ratings.
numPatrons = 0  # keep track of number of patrons
numStarsString = 0

# Get input.


# Convert to double.


# Write while loop here
while numStarsString >= 0:
    numStarsString = int(input("Enter rating for featured movie: "))
    numStars = float(numStarsString)
    if numStarsString < 0:
        break
# Calculate average star rating
    totalStars += numStars
    numPatrons += 1
    
    averageStars = totalStars / numPatrons
    

print("Average Star Value: " + str(averageStars))

