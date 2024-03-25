# A program to print out every 7th number in the range n to n+41
# Mwansa Ng'andu
# 09 March 2022

# Obtain starting number user
num1 = eval(input("Enter a number: \n"))

if -6<num1<2:
    for num1 in range (num1, num1+41, 7):
        print(f"{num1:2}")
        