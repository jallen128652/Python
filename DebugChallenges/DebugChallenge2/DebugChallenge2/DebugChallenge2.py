#Program: DebugChallenge2
#Course: ITSE 1302 7P1
#Author: James Allen
#Description: This program should calculate and display
# the total monthly cost of home ownership. If the total payment
# exceeds the monthy limit, display an appropriate message.
# If the total payment does not exceed the monthly limit, display
# an appropriate message.  There are five bugs/errors in this program.

MONTHLY_LIMIT = 1200.00

mortgagePayment = float(input("Enter mortgage payment: "))
otherPayments = float(input("Enter combined utility, upkeep and taxes: "))

total = mortgagePayment + otherPayments 

print("Total is " + str(total))
print("Limit is " + str(MONTHLY_LIMIT))

if total > MONTHLY_LIMIT:
    print("Cost of ownership exceeds the limit.")
else:
    print("Cost of ownership does not exceed the limit.")
