#Program: KayakRental
#Course: ITSE 1302 7P1
#Author: James Allen
#Description: This program determines rental eligibility

#declare variables

customer1Age = 0
customer1weight = 0
customer2Age = 0
customer2weight = 0
totalWeight = 0

# add inputs 

customer1Age = int(input("Enter customer 1 age: "))
customer1weight = int(input("Enter customer 1 weight: "))
customer2Age = int(input("Enter customer 2 age: "))
customer2weight = int(input("Enter customer 2 weight: "))

# expression

totalWeight = customer1weight + customer2weight

# control structures

if customer1Age >= 18 or customer2Age >= 18:
    if totalWeight <= 450:
        print("Customer may rent the tandom kayak.")
    else:
        print("Can not rent: Combined weight exceeds 450 lbs")
else:
    print("Can not rent: At least one passenger needs to be 18 or over.")


