#Program: Discretionary Spending
#Course: ITSE 1302 7P1
#Author: James Allen
#Description: Program calculates remaining discretionary money

#prompts and inputs
print("Enter pay amount: ")
pay = float(input())
print("Enter rent amount: ")
rent = float(input())
print("Enter utilities amount: ")
utilities = float(input())
print("Enter groceries amount: ")
groceries = float(input())
print("Pay: $" + "{:.2f}".format(pay))
#variable calculation expression and outputs
totalBills = float(rent + utilities + groceries) 
print("Total bills is: $" + "{:.2f}".format(totalBills))
discretionary = float(pay - totalBills)
print("Discretionary: $" + "{:.2f}".format(discretionary))
#the format forces 2 decimal places for dollar values