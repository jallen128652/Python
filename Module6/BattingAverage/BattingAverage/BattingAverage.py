# Declare a named constant for array size here.
MAX_AVERAGES = 8

# Declare array here.
averages = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
minAverage = 999
maxAverage = -1
total = 0
# Write a loop to get batting averages from user and assign to array.
for x in range(0, MAX_AVERAGES):
    averages[x] = float(input("Enter a batting average: "))
    # Assign value to array.
    if averages[x] > maxAverage:
        maxAverage = averages[x]
    if averages[x] < minAverage:
        minAverage = averages[x]
    total = total + averages[x]
averageBattingAverage = total / MAX_AVERAGES
# Assign the first element in the array to be the minimum and the maximum.
print("Minimum batting average is " + str(minAverage))
print("Maximum batting average is " + str(maxAverage))
print("Average batting average is " + str(averageBattingAverage))
# Start out your total with the value of the first element in the array.

# Write a loop here to access array values starting with averages[1]

    # Within the loop test for minimum and maximum batting averages.




    # Also accumulate a total of all batting averages.


# Calculate the average of the 8 batting averages.

