# NewMultiply.py - This program prints the numbers 0 through 10 along
# with these values multiplied by 2 and by 10.
# Input:  None
# Output: Prints the numbers 0 through 10 along with their values multiplied by 2 and by 10. 

#head1 = "Number: "
#head2 = "Multiplied by 2: "
#head3 = "Multiplied by 10: "

#NUM_LOOP_START = 0  # Constant used to control loop
#NUM_LOOP_END = 10 # Constant used to control loop

#print("0 through 10 multiplied by 2 and by 10.")

# Write your for loop here
for head1 in range(0, 10, 1):
    head2 = head1 * 2
    head3 = head1 * 10
    print("Number: " + str(head1))
    print("Multiplied by 2: " + str(head2))
    print("Multiplied by 10: " + str(head3))
