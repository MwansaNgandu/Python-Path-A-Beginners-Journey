month = input ("Enter the month ('January', ..., 'December'): \n") # Obtain month from the user
day = input ("Enter the start day ('Monday', ..., 'Sunday'): \n") # Obtain starting day from user

print (month) # Print month given by the user

# This format will be executed if start day given by user is Monday
if day == 'Monday':
    print ("Mo Tu We Th Fr Sa Su")
    for x in range (1, 8):
        print (f"{x:2}", '', end='') # Print 1st week of month
    print ()    
    for x in range (8, 15):
        print (f"{x:2}", '', end='') # Print 2nd week of month
    print ()   
    for x in range (15, 22):
        print (f"{x:2}", '', end='') # Print 3rd week of month
    print ()    
    for x in range (22, 29):
        print (f"{x:2}", '', end='') # Print 4th week of month
    print () 
    if month == 'February':
        print (f"{'':20}") # Print 5th week of month that 'is Febraury' with spaces
        print (f"{'':20}") # Print 6th week of month that 'is Febraury' with spaces
    elif month == 'April'  or month == 'June' or month == 'September' or month == 'November':
        for x in range (29, 31):
            print (f"{x:2}", '', end ='') # Print 5th week of month with 30 days
        print (f"{'':20}") # Print 6th week of month with 30 days
    if month == 'January'  or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
        for x in range (29, 32):
            print (f"{x:2}", '', end='') # Print 31st day of months with 31 days
        print (f"{'':12}") # Print 5th week of month with 31 days
        print (f"{'':20}") # Print 6th week of month with 31 days
        
# This format will be executed if start day given by user is Tuesday
if day == 'Tuesday':
    print ("Mo Tu We Th Fr Sa Su")
    print (f"{'':2}", '', end='') # Print empty placeholder for Monday
    for i in range (1, 7):
        print (f"{i:2}", '', end='') # Print 1st week of month
    print ()    
    for x in range (7, 14):
        print (f"{x:2}", '', end='') # Print 2nd week of month
    print ()   
    for x in range (14, 21):
        print (f"{x:2}", '', end='') # Print 3rd week of month
    print ()    
    for x in range (21, 28):
        print (f"{x:2}", '', end='') # Print 4th week of month
    print ()
    if month == 'February':
        print ('28', f"{'':18}") # Print 5th week of month that 'is Febraury' with spaces
        print (f"{'':20}") # Print 6th week of month that 'is Febraury' with spaces
    if month == 'April'  or month == 'June' or month == 'September' or month == 'November':
        for x in range (28, 31):
            print (f"{x:2}", '', end ='') # Print 5th week of month with 30 days
        print (f"{'':20}") # Print 6th week of month with 30 days
    if month == 'January'  or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
        for x in range (28, 32):
            print (f"{x:2}", '', end='') # Print 31st day of months with 31 days
        print (f"{'':9}") # Print 5th week of month with 31 days
        print (f"{'':20}") # Print 6th week of month with 31 days
        
# This format will be executed if start day given by user is Wednesday
if day == 'Wednesday':
    print ("Mo Tu We Th Fr Sa Su")
    print (f"{'':5}", '', end='') # Print 2 empty placeholders for Monday and Tuesday
    for x in range (1, 6):
        print (f"{x:2}", '', end='') # Print 1st week of month
    print ()    
    for x in range (6, 13):
        print (f"{x:2}", '', end='') # Print 2nd week of month
    print ()   
    for x in range (13, 20):
        print (f"{x:2}", '', end='') # Print 3rd week of month
    print ()    
    for x in range (20, 27):
        print (f"{x:2}", '', end='') # Print 4th week of month
    print ()
    if month == 'February':
        print ('27 ', '28', f"{'':15}") # Print 5th week of month that 'is Febraury' with spaces
        print (f"{'':20}") # Print 6th week of month that 'is Febraury' with spaces
    if month == 'April'  or month == 'June' or month == 'September' or month == 'November':
        for x in range (27, 31):
            print (f"{x:2}", '', end ='') # Print 5th week of month with 30 days
        print (f"{'':20}") # Print 6th week of month with 30 days
    if month == 'January'  or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
        for x in range (27, 32):
            print (f"{x:2}", '', end='') # Print 31st day of months with 31 days
        print (f"{'':6}") # Print 5th week of month with 31 days
        print (f"{'':20}") # Print 6th week of month with 31 days
        
# This format will be executed if start day given by user is Thursday
if day == 'Thursday':
    print ("Mo Tu We Th Fr Sa Su")
    print (f"{'':8}", '', end='') # Print 3 empty placeholders for Monday, Tuesday and Wednesday
    for i in range (1, 5):
        print (f"{i:2}", '', end='') # Print 1st week of month
    print ()    
    for x in range (5, 12):
        print (f"{x:2}", '', end='') # Print 2nd week of month
    print ()   
    for x in range (12, 19):
        print (f"{x:2}", '', end='') # Print 3rd week of month
    print ()    
    for x in range (19, 26):
        print (f"{x:2}", '', end='') # Print 4th week of month
    print ()
    if month == 'February':
        print ('26 ', '27 ', '28', f"{'':12}") # Print 5th week of month that 'is Febraury' with spaces
        print (f"{'':20}") # Print 6th week of month that 'is Febraury' with spaces
    if month == 'April'  or month == 'June' or month == 'September' or month == 'November':
        for x in range (26, 31):
            print (f"{x:2}", '', end ='') # Print 5th week of month with 30 days
            print (f"{'':20}") # Print 6th week of month with 30 days
    if month == 'January'  or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
        for x in range (26, 32):
            print (f"{x:2}", '', end='') # Print 31st day of months with 31 days
        print (f"{'':3}") # Print 5th week of month with 31 days
        print (f"{'':20}") # Print 6th week of month with 31 days
        
# This format will be executed if start day given by user is Friday
if day == 'Friday':
    print ("Mo Tu We Th Fr Sa Su")
    print (f"{'':11}", '', end='') # Print 4 empty placeholders for Monday, Tuesday, Wednesday and Thursday
    for i in range (1, 4):
        print (f"{i:2}", '', end='') # Print 1st week of month
    print ()    
    for x in range (4, 11):
        print (f"{x:2}", '', end='') # Print 2nd week of month
    print ()   
    for x in range (11, 18):
        print (f"{x:2}", '', end='') # Print 3rd week of month
    print ()    
    for x in range (18, 25):
        print (f"{x:2}", '', end='') # Print 4th week of month
    print ()
    if month == 'February':
        print ('25 ', '26 ', '27 ', '28', f"{'':9}") # Print 5th week of month that 'is Febraury' with spaces
        print (f"{'':20}") # Print 6th week of month that 'is Febraury' with spaces
    if month == 'April'  or month == 'June' or month == 'September' or month == 'November':
        for x in range (25, 31):
            print (f"{x:2}", '', end ='') # Print 5th week of month with 30 days
        print (f"{'':3}")
        print (f"{'':20}") # Print 6th week of month with 30 days
    if month == 'January'  or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
        for x in range (25, 32):
            print (f"{x:2}", '', end='') # Print 31st day of (in the 5th week) months with 31 days
        print ()
        print (f"{'':20}") # Print 6th week of month with 31 days
        
# This format will be executed if start day given by user is Saturday
if day == 'Saturday':
    print ("Mo Tu We Th Fr Sa Su")
    print (f"{'':14}", '', end='') # Print 5 empty placeholders for Monday, Tuesday, Wednesday, Thursday and Friday
    for i in range (1, 3):
        print (f"{i:2}", '', end='') # Print 1st week of month
    print ()    
    for x in range (3, 10):
        print (f"{x:2}", '', end='') # Print 2nd week of month
    print ()   
    for x in range (10, 17):
        print (f"{x:2}", '', end='') # Print 3rd week of month
    print ()    
    for x in range (17, 24):
        print (f"{x:2}", '', end='') # Print 4th week of month
    print ()
    if month == 'February':
        for x in range (24, 29):
            print (f"{x:2}", '', end ='') # Print 5th week of month that 'is Febraury' with spaces
        print (f"{'':6}")
        print (f"{'':20}") # Print 6th week of month that 'is Febraury' with spaces
    if month == 'April'  or month == 'June' or month == 'September' or month == 'November':
        for x in range (24, 31):
            print (f"{x:2}", '', end ='') # Print 5th week of month with 30 days
        print (f"{'':20}") # Print 6th week of month with 30 days
    if month == 'January'  or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
        for x in range (24, 31):
            print (f"{x:2}", '', end='') # Print 31st day of (in the 5th week) months with 31 days
        print ()
        print ("31", f"{'':18}") # Print 6th week of month with 31 days
        
# This format will be executed if start day given by user is Sunday
if day == 'Sunday':
    print ("Mo Tu We Th Fr Sa Su")
    print (f"{'':17}", '', end='') # Print 6 empty placeholders for Monday, Tuesday, Wednesday, Thursday, Friday and Saturday
    for x in range (1, 2):
        print (f"{x:2}", '', end='') # Print 1st week of month
    print ()    
    for x in range (2, 9):
        print (f"{x:2}", '', end='') # Print 2nd week of month
    print ()   
    for x in range (9, 16):
        print (f"{x:2}", '', end='') # Print 3rd week of month
    print ()    
    for x in range (16, 23):
        print (f"{x:2}", '', end='') # Print 4th week of month
    print ()
    if month == 'February':
        for x in range (23, 29):
            print (f"{x:2}", '', end ='') # Print 5th week of month that 'is Febraury' with spaces
        print (f"{'':3}")
        print (f"{'':20}") # Print 6th week of month that 'is Febraury' with spaces
    if month == 'April'  or month == 'June' or month == 'September' or month == 'November':
        for x in range (23, 30):
            print (f"{x:2}", '', end ='') # Print 5th week of month with 30 days
        print ('30', f"{'':18}") # Print 6th week of month with 30 days
    if month == 'January'  or month == 'March' or month == 'May' or month == 'July' or month == 'August' or month == 'October' or month == 'December':
        for x in range (23, 30):
            print (f"{x:2}", '', end='') # Print 31st day of (in the 5th week) months with 31 days
        print ()
        print ('30', "31", f"{'':15}") # Print 6th week of month with 31 days