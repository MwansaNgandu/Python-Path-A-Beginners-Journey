# A program that calculates the value of PI and then computes and displays the area of a circle with radius entered by the user
# Mwansa Ng'andu
# 02 March 2022

from math import sqrt

a = 2

num1 = sqrt(a)
num2 = sqrt(a + num1)
num3 = sqrt(a + num2)

# Calculate the value of PI
PI = a*(a/num1)*(a/num2)*(a/num3) 

# Round of the value of PI to 4 digits
PI_4 = round (PI, 4) 

print ("Approximation of pi:", PI_4)

# Obtain the radius from the user
radius = eval(input("Enter the radius: \n"))

# Calculate the value of the area
area = PI*radius*radius

print ("Area:", round (area, 4))