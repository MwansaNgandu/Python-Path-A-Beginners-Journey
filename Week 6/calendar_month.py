# A program to print out a calendar
# Mwansa Ng'andu
# 06 April 2022

import math
import calendar

def day_of_week(day, month, year):
    ''' Given a date consisting of day of month, month number and year, 
        return the day of the week on which it falls
    '''
    h = (day + math.floor(13*(month+1)/5) + year + math.floor(year/4) - math.floor(year/100) + math.floor(year/400)) # Zeller’s congruence
    no_day = ((h+5) % 7) + 1 
    return no_day

def is_leap(year):
    '''Given a year return True if it is a leap year, False otherwise. 
       This function returns a Boolean value
    '''
    return calendar.isleap(year)

def month_num(month_name):
    '''return the month number
    '''    
    global num
    a = month_name.title()
    month = ["Unknown", "January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"] # Create a plave holder for position 0
    for x in month:
        if x == a:
            num = month.index(a)
            return num

def num_days_in(month_num, year): 
    '''Return number of days in that month in that year
    '''
    _DAYS_IN_MONTH = [-1, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    assert 1 <= month_num <= 12, month_num
    if month_num == 2 and is_leap(year) == True:
        return 29
    return _DAYS_IN_MONTH[month_num]

def num_weeks(month_num, year):
    '''return the number of weeks that the month spans
    '''    
    from calendar_month import num_weeks
    from calendar_month import day_of_week    
    last_digit = (8-day_of_week(1, month_num, year)) # Determine last digit of the first week
    a = (num_days_in(month_num, year) - last_digit)//7 # Find number of full 7 day weeks
    return a + 2

def week(week_num, start_day, days_in_month):
    '''Return a string consisting of the day of the month for each day in that week, 
       starting with Monday and ending with Sunday
    '''
    # first week
    spaces_taken = start_day*-3 +23 # Find spaces taken by dates in week 1
    last_digit = spaces_taken - (8-start_day) - (-start_day+7)  # Last digit of week 1   
    spaces_1 = start_day*3-3 # Spaces before list of dates in week 1
    if week_num == 1:
        print (f"{' ':1}"*spaces_1, end='')
        for x in range (1, last_digit+1):
            print (f"{' '+str(x):3}", end='') # Print 1st week of month
        print ()    

    # last week
    if week_num == val_weeks:
        for l in range (last_digit+(7*(week_num-1))-6, days_in_month+1):
            print (f"{l:2}", '', end='')
        print ()
   
    # middle weeks
    elif week_num >1 and week_num < val_weeks:
        for m in range (last_digit+(7*(week_num-1))-6, last_digit+(7*(week_num-1))+1):
            print (f"{m:2}", '', end='')
        print ()
    
def main():
    '''print the calendar for that month by obtaining the number of weeks and then obtaining the week string for each
    '''
    global start_day
    global num_days 
    global val_weeks
    month_name = input('Enter month:\n')
    year = eval (input('Enter year:\n'))
    print (month_name.title())
    print ('Mo Tu We Th Fr Sa Su')
    val_month = month_num(month_name)
    start_day = day_of_week(1, val_month, year)
    num_days = num_days_in(val_month, year)
    val_weeks = num_weeks(val_month, year)
    for s in range (1, val_weeks+1):
        week(s, start_day, num_days)

if __name__=='__main__':
    main()






