# A program that asks the user to enter the lengths 𝑎 and 𝑐, and calculates 𝑏
# Mwansa Ng'andu
# 02 March 2022

from math import sqrt

# Obtain side a from user
a = eval(input("Enter the length of side a: \n")) # This is the hypotenuse.

# Obtain side c from user
c = eval(input("Enter the length of side c: \n"))

if a <= 0 or c <= 0:
    print ("Sorry, lengths must be positive numbers.")
    
elif a > c:
    b = sqrt(a*a - c*c) # Calculate side b if a > c
    print ("The length of side b is", b)

elif a <= c:
    b_2 = sqrt(c*c - a*a) # Calculate side b if a <=c
    print ("The length of side b is", b_2, end='') 
    print (".")
