# Sheldon D'Souza
# Objective of the weekly task is to display a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.
# I have assumed that 4 elements need to be plotted range [0,4] although range(0,4) would exclude the last element 4.
# The graph can be plotted using numpy functions as well as using lists with for loops
# I have for the purposes of demonstration used one of each although it would be simpler here to use numpy only
# I used some of the matplotlib.org, datacamp.com and realpython tutorials for some of the design items below

import numpy as np
import matplotlib.pyplot as plt


x = np.array([0,1,2,3,4]) # using numpy to create a array with 5 elements i.e in the range from 0 to 4 inclusive

g_x = np.array(x ** 2) # generates g_x as x squared


h_x = [] # define a blank list and fill it using a for loop
x_1 = [] 
for n in range(0,5):
    x_1.append(n) # creates a list for the x axis
    h_x.append(n ** 3) # creates a list for the y axis

# The following code will plot and format:

plt.plot(x, x, color = 'g', label = 'f(x) = x', ls = '--', linewidth = 3.0) #f(x) = x is just a linear graph so x and y will be the same
plt.plot(x, g_x, color='b', label = 'g(x) = x**2', ls = '-.', linewidth = 2.0)
plt.plot(x_1, h_x, color = 'r', label = 'h(x) = x**3', ls = ':', linewidth = 4.0) # Plot the h(x) function using lists and the for loop

plt.title("Plotting Functions", fontsize = 15, loc = 'center')
plt.xlabel("X axis", fontsize = 10)
plt.xlim(0)
plt.ylabel('Y axis', fontsize = 10)
plt.legend(loc='best')

plt.tight_layout()

# plt.savefig('functions.png') # Can add the save function if needed

plt.show()