# A program to draw a text-based graph of a mathematical function f(x)
# Mwansa Ng'andu
# 21 March 2022

import math

# Obtain the function from the user
graph_given = input("Enter a function f(x):\n")

for y in range (10, -11, -1): 
    for x in range (-10, 11):
        f = round(eval(graph_given))
        if x == 0 and y == 0 and y != f: 
            print ("+", end="") # Print the origin of the cartesian plain
        elif y == 0 and y != f:
            print ("-", end="") # Print the horizontal axis (x-axis)
        elif x == 0 and y != f:
            print ("|", end="") # Print the vertical axis (y-axis)
        elif y == f:
            print ("o", end="") # Plot the coordinates of the given function
        else:
            print (" ", end="") # Print an empty space on the cartesian plane where there is no corrseponding coordinate or axis placeholder
    print()