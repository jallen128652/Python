# Program Name: SetsGame
# Program Author: James Allen
# Class: Computer Programming ITSE 1302 7P1
# Description: This program rolls 5 dice for a player and computer and 
# determines who has the highest number of a kind

import random
#Create empty lists that will store player's dice and computer's dice
computerRoll = []
playerRoll = []
#Declare pMatches and cMatches and store zero in them
pMatches = 0
cMatches = 0
pCount = 0
cCount = 0
numDice = 5
#Use them later to store the highest number of matches in the each dice list

#This loop will "roll" 5 dice for the player and computer
#loop 5 times
    #Append a random number between 1 and 6 to player's dice list
    #Append a random number between 1 and 6 to computers's dice list
for x in range(0, numDice):
    roll = random.randint(1,6)
    computerRoll.append(roll)
for x in range(0, numDice):
    roll = random.randint(1,6)
    playerRoll.append(roll)

#This loop determines the highest number of matches in each dice list
#For x = 1 to 6
    #Determine how many times the number x is in the player's list (pCount)
    #Determine how many times the number x is in the computer's dice list (cCount)
    #if pCount is greater than pMatches
        #store pCount in pMatches
    #if cCount is greater than cMatches
        #store cCount in cMatches
for x in range(1, 7):
    cCount = computerRoll.count(x)
    if cCount > cMatches:
        cMatches = cCount
    pCount = playerRoll.count(x)
    if pCount > pMatches:
        pMatches = pCount
        
#Display computer's dice list
print(computerRoll)
#Display player's dice list
print(playerRoll)
#Display number of computer's matches
print("Computer has " + str(cMatches) + " of a kind")
#Display number of player's matches
print("Player has " + str(pMatches) + " of a kind")

#Use an if structure to display if the player won, computer won, or if it was a tie
if pMatches > cMatches:
    print("Player wins")
elif cMatches > pMatches:
    print("Computer wins")
elif cMatches == pMatches:
    print("It is a tie game.")