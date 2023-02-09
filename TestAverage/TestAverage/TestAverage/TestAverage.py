#Program: Test Average
#Course: ITSE 1302 7P1
#Author: James Allen
#Description: Program calculates average test scores

#prompts and inputs
print("Enter test 1 score: ")
test1 = int(input())
print("Enter test 2 score: ")
test2 = int(input())
print("Enter test 3 score: ")
test3 = int(input())
print("Enter test 4 score: ")
test4 = int(input())
#variable calculation expresion
average = float(test1 + test2 + test3 + test4) / 4
#output to the user
print("The average is " + str(average))
