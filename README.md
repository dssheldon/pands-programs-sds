# Programming and Scripting - Weekly Assignments
##### <u>Owner: Sheldon D'Souza</u>



## Objective

The objective of this ReadMe is to set out the layout of the repository and it's contents.
The repository is built up of weekly homework assignments given as part of the Programming and Scripting Module. Each assignment has it's own file which includes the code for the weekly assignment.

I have included a lot explanation of how the code functions within the .py files and therefore I will not repeat this here. Please refer to the individual python scripts within the files and the comments/documentation therein for details on how the codes operates as well as areas I found tricky. I have also included where appropriate references to researched code and solutions.

## Contents of Repository

The contents of this repository are as follows:

### 1. BMI
The task was to calculate the BMI of a person by taking inputs of a person's height in cms and weight in kgs. The program then calculates the BMI of a person.

The program built on concepts on asking for input and using the input in conditional statements (if-then-else)

I added functionality in the program of printing out whether the person was underweight, ideal weight or overweight.

### 2. Second String
The task was to ask a user to input a string and output every letter in reverse order.

This program obtained the user input, added it to a list and then used slicing to return every second letter of the list in reverse by using the [-2] interval within the slicing code.

The code was based on Page 32 of "A Whirlwind Tour of Python" by Jake Vanderplas

### 3. Collatz
This program asks a user to input any positive integer and outputs the successive values of the following calculation: 
* At each step the program will calculate the next value by taking the current value and; 
* if it is even, divides it by two, but if it is odd, multiplies it by three and then adds one. 
* The program ends if the current value is one.

The program will first as for a positive integer. It will then proceed to validate whether the is not negative or zero (i.e. it is indeed a positive integer). This is done through a 'while True' loop and an 'if' statement. The program uses continue and break depending on the outcome of the if statement. If the input is invalid the program will display a message and restart. This section was tricky and I came back to it towards the end of the course.

Once a valid input is received the program will append the input to a list (mylist). The input will the enter a while loop which will perform the necessary calculations on the integer (as mentioned above) appending the result at each iteration to 'mylist'.

Once the value of the calculation reaches 'One', the program print 'mylist' and terminates.

### 4. Weekday
The objective of this program was to write a program that outputs whether or not today (i.e the current day at the time of running the program) is a weekday or not.

I imported the datetime module and returned the index of the current weekday to a variable 'today_index'. I also created a variable to hold tuples of the the names of the days of the week ('week_names').

The output of 'today_index' was routed through an if-then-else statement to check whether this was >5 or not. Based on the value returned by 'today_index' the program printed out the current day of the week, by  printing the index which corresponded to the 'week_names' variable. The program printed out that it was a weekend if the index was >5 (Monday being index 0 etc.)

### 5. Squareroot
The objective of this program was to create a function to take  a positive floating-point number as input and outputs an approximation of its square root.

The program uses Newtons method for finding roots which uses the formula:
````x1 = x0 - f(x0) / f'(x0)````

The program starts by validating the input by using  a while loop to iterate until the user enters a valid input i.e. a non negative or zero number which the program converts to a float.

The formula requires a guess of the square root as and initial number to start off Newton's equation. The program uses half the input number as a first guess (This part was tricky and required research as well we as trial and error) and iterates through the formula to arrive at the estimated square root. The iterations were completed using a while loop.

Newton's method gets closer to the square root the more it iterates, however in order to build an efficient program, it should stop after the required level of precision has been achieved. Therefore using a 'for' loop could be wasteful for some numbers input and incorrect for others.

In order to achieve a precision level of (say) 4 decimal places, as used in the program, I created an empty list and appended the output of each iteration to the list (rounded down to the precision level). At each iteration the program compared the value appended to the previous value of the list. The program terminated when the current value of the list equaled the previous list value, which indicated that the precision level had been achieved.

This program required a considerable amount of research and thought especially to achieve the make the program efficient, as described above.


### 6. E's
The objective was to write a  program that reads in a text file and outputs the number of e's it contains. The program was required to  take the filename from an argument on the command line. I amended the program slightly to take in a user input search character but the default remaining as 'e'. (Reference: Week 7 Lectures and Real Python blog post)

Obtained the mobydick.txt file from ftp://ftp.cs.princeton.edu/pub/cs226/textfiles/mobydick.txt

I imported the  Path from the pathlib library so that the input could take a full file path rather than only a file name

The user is asked for the path of the file they want to search and the character they want to search for (The default character was set as 'e').

The program then opens the file using the 'with open' command and uses the .read() method to read the contents of the file to a variable. The program then uses a 'for' loop to iterate though the text of the file and uses an 'if' statement to append matching characters to the list created.

Once the 'for' loop is complete the program prints  the length of the list, which is the number of instances of the search character.

### 7. Plotting
The objective was to write a program that displays a plot of the functions f(x)=x, g(x)=x2 and h(x)=x3 in the range [0, 4] on the one set of axes.

I imported the pyplot from the matplotlib library as well as numpy.

The plot can be derived by using numpy as well as using a standard for loop to generate a list of the number from the function. I have  used both approaches although the numpy approach would be easier and more efficient to use.

###### Generating the function via the 'for' loop:

This entailed building a for loop within a and using the range function for the loop to iterate through the numbers 0 to 4 (inclusive). Each loop appends the number to one list and the cube of the number (for the h(x) function above) into the second list.

###### Generating the function via numpy:

Generated a numpy array for numbers from 0 to 4 (inclusive). The function was generated by performing calculations on the array.

###### Plotting:

Used the pyplot plot function from matplotlib to generate the plots using arguments of the function to generate the colour of the line, the label of the plot (which was used to populate the legend), line style (or the type of the line plotted e.g. dashed etc.) and line width.

Used further plotting functions to add a title to the plot (using arguments to specify the fontsize and the location of the title), set the x and y labels, added a legend and set the x starting limit as zero.

By adding the code for the plots consecutively using the stateful approach of matplotlib, the plots were superimposed over each other this adding all three plots on the same axes.

Finally added the tight_layout functionality and set the plot to show.