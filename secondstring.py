# The objective of the program is to take a string from a user and
#   return every second character in reverse
# Based on Page 32 of "A Whirlwind Tour of Python" by Jake Vanderplas

mystring = input('Please input your desired text: ') # Asks users to input a string

rev_mystring = mystring[-1::-2] # starts off on the last character of a string (-1 index) and skips 1 character to return every second character

print(rev_mystring) # prints the new string
