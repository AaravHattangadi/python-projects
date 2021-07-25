# Python Leap Year Checker
# Aarav Hattangadi 2021
# github.com/AaravHattangadi




yearstr = input("Input a Year") # Asks user for the year - input(); Stores the users input in the variable 'yearstr' in a string format.

year = int(yearstr) # Converts 'yearstr' (string format) into integer format


# If-Else statement is used to check
if (year % 4) == 0: # checks if the year is divisible by 0; If yes, it continues; If no, it jumps to line 22-23
    if (year % 100) == 0: # Checks if the year is divisble by 100; If yes, it continues; if no, it jumps to line 20-21
        if (year % 400) == 0: # Checks if the year is divisible by 400; If yes, it continues; If no, it jumpes to line 18-19
            print("{0} is a leap year".format(year)) # Prints argument 0 {0}, that is the var 'year' followed by the string, is a leap year. This argument is the formatted into a preset year format by the command ".format(year)"
        else:
            print("{0} is not a leap year".format(year)) # Prints argument 0 {0}, that is the var 'year' followed by the string, is not a leap year. This argument is the formatted into a preset year format by the command ".format(year)"
    else:
        print("{0} is a leap year".format(year)) # Prints argument 0 {0}, that is the var 'year' followed by the string, is a leap year. This argument is the formatted into a preset year format by the command ".format(year)"
else:
    print("{0} is not a leap year".format(year)) # Prints argument 0 {0}, that is the var 'year' followed by the string, is not a leap year. This argument is the formatted into a preset year format by the command ".format(year)"