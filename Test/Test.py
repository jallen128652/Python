#defines the pay and taxes function along with two parameters
def pay_and_taxes(gross_pay, tax_rate):
    # does the math
    taxes = gross_pay * (tax_rate / 100)
    net_pay = gross_pay - taxes
    # displays values
    print(f'Your Gross Pay was ${gross_pay:,.2f}')
    print(f'You owe ${taxes:,.2f} in taxes.')
    print(f'Your take home pay for the year is ${net_pay:,.2f}')
#primes the loop    
yearly_pay = 1
# loop has sentinal value
while yearly_pay != 0: 
    # takes user input in correct format    
    yearly_pay = float(input("Enter your yearly pay or enter 0 to end the program: "))
    # ends the loop and thanks user
    if yearly_pay == 0:
        print("Thanks for trying the program!")        
    else:
       # continues the loop iteration
       tax_percent = float(input("Enter your tax rate as a percentage: "))  
       # calls function and passes var values as parameters into the function
       pay_and_taxes(yearly_pay, tax_percent) 
    
#note it will still ask for a tax_percent even after entering the sentinal value