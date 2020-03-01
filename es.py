# Sheldon D'Souza
# G00387857
# Weekly task 7
# The objective of the task is to write a program that reads a text file and outputs the number of 'e's it contains
# I amended the program slightly to take in a user input search character but the default remaining as e
# As instructed the program will take the filename on the command line
# Reference: Week 7 Lectures and Real Python blog post
# Obtained the mobydick.txt file from ftp://ftp.cs.princeton.edu/pub/cs226/textfiles/mobydick.txt
# I added on a step importing Path from the pathlib library so that the input could take a full file path rather than only a file name
#   I googled how to do this  

from pathlib import Path
file_name = Path(input('Please enter the name and path of the file: ')) # ask user to input the file name
search_char = input('Please enter the search character (press enter to select "e"): ') # takes a user input search character
if search_char == '': # if no search character is input then
    search_char = 'e' #   the default search character will be e

with open(file_name, 'r') as search_file: # opens the file
    search_file_text = search_file.read() # reads the file and stores the text in a variable
    list_for_ss = [] # create an empty list to store the number times the search character occurs
    for text in search_file_text: # iterates through the text within the open file
        if text == search_char: # searches for each iteration of the search character in the search text 
            list_for_ss.append(text) # appends all positive hits into the specified list
    print('The number of times', search_char, 'appears in', file_name.name, 'is', len(list_for_ss)) # prints the length of the list