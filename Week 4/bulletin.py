# A program to simulate a simple BBS with one stored message and 2 fixed files
# Mwansa Ng'andu
# NGNMWA001
# 02 March 2022

# Print the menu
print ("Welcome to UCT BBS")
print ("MENU") 
print ("(E)nter a message")
print ("(V)iew message")
print ("(L)ist files")
print ("(D)isplay file")
print ("e(X)it")

# Obtain users selection from menu
user_selection = input ("Enter your selection:\n")
message = 0
while user_selection != 'x':
    if user_selection == 'e':
        message = input ("Enter the message:\n")
        print ("Welcome to UCT BBS") # Print the welcome and menu
        print ("MENU") 
        print ("(E)nter a message")
        print ("(V)iew message")
        print ("(L)ist files")
        print ("(D)isplay file")
        print ("e(X)it") 
        user_selection = input ("Enter your selection:\n")
    if user_selection == 'v':
        if message == 0:
            print ("The message is: no message yet") # Print user has not yet entered a message
        else: 
            message !=0
            print ("The message is:", message) # Print if user has entered a message
        print ("Welcome to UCT BBS") # Print the welcome and menu
        print ("MENU") 
        print ("(E)nter a message")
        print ("(V)iew message")
        print ("(L)ist files")
        print ("(D)isplay file")
        print ("e(X)it") 
        user_selection = input ("Enter your selection:\n")
    if user_selection == 'l':
        print ("List of files: 42.txt, 1015.txt") # List available files to display
        print ("Welcome to UCT BBS") # Print the welcome and menu
        print ("MENU") 
        print ("(E)nter a message")
        print ("(V)iew message")
        print ("(L)ist files")
        print ("(D)isplay file")
        print ("e(X)it")   
        user_selection = input ("Enter your selection:\n")
    if user_selection == 'd':
        file_name = input ("Enter the filename:\n")
        if file_name == '42.txt':
            print ("The meaning of life is blah blah blah ...")     
            print ("Welcome to UCT BBS") # Print the welcome and menu
            print ("MENU") 
            print ("(E)nter a message")
            print ("(V)iew message")
            print ("(L)ist files")
            print ("(D)isplay file")
            print ("e(X)it") 
            user_selection = input ("Enter your selection:\n")
            continue
        elif file_name == '1015.txt':
            print ("Computer Science class notes ... simplified")
            print ("Do all work")
            print ("Pass course")
            print ("Be happy")  
            print ("Welcome to UCT BBS") # Print the welcome and menu
            print ("MENU") 
            print ("(E)nter a message")
            print ("(V)iew message")
            print ("(L)ist files")
            print ("(D)isplay file")
            print ("e(X)it") 
            user_selection = input ("Enter your selection:\n")
            continue
        elif file_name != '42.txt' or file_name != '1015.txt' :
            print ("File not found") # Print if requested file is not included in list
            print ("Welcome to UCT BBS") # Print the welcome and menu
            print ("MENU")  
            print ("(E)nter a message")
            print ("(V)iew message")
            print ("(L)ist files")  
            print ("(D)isplay file")
            print ("e(X)it") 
            user_selection = input ("Enter your selection:\n")
            continue
    if user_selection == 'x':
        print(end='')
print ("Goodbye!")      