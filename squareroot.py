# Sheldon D'Souza
# I started out by researching Newtons method for finding roots
# I coded in the equation for Newton's method which uses the formula:
# x1 = x0 - f(x0) / f'(x0)
# I then used a for loop for the iterations to get closer to desired answer


def sqrt():
	
	# asked for user input as per instructions. We can also ask for an argument 
	# to be specified while defining the function
	# added a while loop to validate whether to validate whether the number is positive.
	# If the number is neagtive the program will display a message and repeat the loop asking for the number again.

	is_positive = True
	while is_positive:
		positive_number = float(input('Please enter a positive number: '))
		if positive_number < 1: # I chose 1 here as I also wanted to exclude 0 from the user input as it will give a 'div by zero' error
			 print('The number you have entered is not a positive number')
		else:
			is_positive = False	 

	
	# The following code will be the first guess for the number. 
	# This part was a bit tricky but after some research I was able to settle on half the intial number as a good first guess
	
	positive_number_guess = (positive_number) / 2
	
	# The for loop will use the guess as a start and get closer to the answer after each iteration 
	# (This is part of Newton's method which is meant to get closer to the appoximate root after each iteration)

	for n in range (1,100):
		real_f = (positive_number_guess ** 2) - positive_number
		derivative_f = 2 * positive_number_guess
		positive_number_guess = positive_number_guess - (real_f / derivative_f)

	# printed the desired output
	
	print('The squareroot of', positive_number, 'is appoximately', round(positive_number_guess, 6))

sqrt()  # calls the function