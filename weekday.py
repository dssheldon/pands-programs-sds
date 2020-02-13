import datetime # Importing datetime module

# the next line looks to use the weekday function from within the datetime 
# module to get and index relating to the day if the week.
# 0 being Monday, 1 being Tuesday etc.
# I googled the functionality and researched various examples of the use of datetime.


today_index = datetime.datetime.today().weekday()

# The next line prepares a tuple of the names of the week to match the index value returned from the variable today_index.
# This can also be prepared as a list. The purpose of using a tuplemis to make it non-mutable

week_names = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

# The following if else block evaluates whether the return value from today_index is greater or less than 5.
# As the only values above 5 will correspond to Saturday and Sunday the block prints out the appropriate messages based on this logic

if today_index > 5:
	print('Today is', week_names[today_index], 'and it is the weekend')
else:
	print('Today is', week_names[today_index], 'and unfortunately is a weekday')

