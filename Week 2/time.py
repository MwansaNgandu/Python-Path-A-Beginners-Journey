# A program for checking the validity of a time entered by the user as a set of three integers
# Mwansa Ng'andu
# 02 March 2022

# Obtain hours from user
hours = eval(input("Enter the hours: \n"))
             
# Obtain minutes from user
minutes = eval(input("Enter the minutes: \n"))

# Obtain seconds from user
seconds = eval(input("Enter the seconds: \n"))

A = hours >= 0 and hours <= 23
B = minutes >= 0 and minutes <= 59
C = seconds >= 0 and seconds <= 59

if A and B and C:
    print ("Your time is valid.")
else: print ("Your time is invalid.")