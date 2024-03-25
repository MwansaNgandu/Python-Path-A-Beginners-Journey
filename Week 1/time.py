# Program to convert an amount of minutes into an equivalent amount of days, hours and minutes.
# Mwansa Ng'andu
# 22 February 2022

# Obtain minutes from the user
input_str = input("Enter a quantity of minutes: ")
minutes = int(input_str)

# Calculate the equivalent amount of hours and days 
hours = minutes//60
days = hours//24

minutes = minutes%60
hours = hours%24

# Print the amount of minutes into the equivalent amount of days, hours and minutes
print("The number of days is", days, end=', ')
print("the number hours is", hours, end=', ')
print("and the number of minutes is", minutes, end='')
print(".")



