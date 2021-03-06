# This program asks a user to input any positive integer and outputs the successive values of the following calculation: 
# At each step the program will calculate the next value by taking the current value and; 
# if it is even, divides it by two, but if it is odd, multiplies it by three and then adds one. 
# The program ends if the current value is one.

# Researched how to restart the program if invalid input was given. Achieved this through a while True loop (with break and continue)


mylist = [] # creates an empty list

while True: # used a while True loop with break and continue to validate the input
    mynumber = int(input('Please input any positive integer: ')) # Asks the user to input a number and then converts it into an integer
    if mynumber <= 0: # This block checks that the number is not negative or zero. If it is then the program restarts. 
        print('You have inserted a negative number or zero. Please try again.')
        continue # If invalid input the  program restarts
    else:
        break

mylist.append(mynumber) # Adds the user inputed number as the first item of the list

while mynumber != 1: # While loop to check for the conditions specified in the program
    if mynumber % 2 == 0:
        mynumber = int(mynumber / 2)
    else:
        mynumber = int(((mynumber * 3) + 1))
    mylist.append(mynumber) # Append the output from the conditional test above to the list

print(mylist) # Prints the final list of all numbers.