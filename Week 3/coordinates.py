# A program that checks if a set of six numbers is a pair of geographical/GPS coordinates or not
# Mwansa Ng'andu
# 02 March 2022

# Obtain degrees lat. from user
num1 = eval(input("Enter first number: \n"))

# Obtain minutes lat. from user
num2 = eval(input("Enter second number: \n"))

# Obtain seconds lat. from user
num3 = eval(input("Enter third number: \n"))

# Obtain degrees long. from user
num4 = eval(input("Enter fourth number: \n"))

# Obtain minutes long. from user
num5 = eval(input("Enter fifth number: \n"))

# Obtain seconds long. from user
num6 = eval(input("Enter sixth number: \n"))

A = -90<=num1<=90
B = 0<=num2<=59
C = 0<=num3<=59
D = -180<=num4<=180
E = 0<=num5<=59
F = 0<=num6<=59

if A and B and C and D and D and E and F:
    print("WOW! Looks like geographic coordinates!")
else: print("Hmmm ... looks like 6 random numbers.")