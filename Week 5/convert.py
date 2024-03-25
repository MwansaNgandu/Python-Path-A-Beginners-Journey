# A program that converts a date and time given in a 24-hour format to form a 12-hour format
# Mwansa Ng'andu
# 21 March 2022

# Obtain date and time from user
a = str (input ("Enter the date and time (yyyy-mm-dd hh:mm):\n"))

# am hours of the day 
if ord (a[11]) == 48 and ord (a[12]) != 48: # if hours of the morning begin with zero
    am_pm = 'am'
    time = a[12]+':'+a[14:16]
elif eval (a[11:13]) < 12 and ord (a[11]) != 48: # if hours of the morning are 10 or 11 
    am_pm = 'am'
    time = a[11:16]
elif eval (a[11:13]) == 24 and ord (a[11]) != 48 or eval (a[11:13]) == 00: # if hour the day is midnight 
    am_pm = 'am'
    time = '12:'+a[14:16]
    
# pm hours of the day    
elif eval (a [11:13]) >= 22 and eval (a [11:13]) < 24 and ord (a[11]) != 48: # if hours of the evening are 22 or 23
    am_pm = 'pm'
    time =  chr(ord (a[11])-ord('2')+ ord('1'))+chr(ord (a[12])-ord('2')+ ord('0'))+':'+a[14:16]
elif eval (a [11:13]) == 20 or eval (a [11:13]) == 21 and ord (a[11]) != 48: # if hours of the evening are 21 or 20
    am_pm = 'pm'
    time =  chr(ord (a[12])-ord('0')+ ord('8'))+':'+a[14:16]
elif eval (a [11:13]) > 12 and eval (a [11:13]) < 20 and ord (a[11]) != 48: # if hours of the afternoon are from 13 to 19
    am_pm = 'pm'
    time =  chr(ord (a[12])-ord('2')+ ord('0'))+':'+a[14:16]
elif eval (a [11:13]) == 12 and ord (a[11]) != 48: # if hour of the afternoon is 12
    am_pm = 'pm'
    time = a[11:16]
    
# print format for the day of the month
if eval (a [9]) ==  1 and eval (a[8]) != 1: # for days that end on 1 excluding 11
    if eval (a [8]) ==  0:
        day = a[9]+'st'
    else:
        if eval (a[8:10]) != 11:
            day = a [8:10]+'st'
elif eval (a [9]) ==  2 and eval (a[8]) != 1: # for days that end on 2 excluding 12
    if eval (a [8]) ==  0:
        day = a[9]+'nd'
    else:
        if eval (a[8:10]) != 11:
            day = a [8:10]+'nd'
elif eval (a [9]) ==  3 and eval (a[8]) != 1: # for days that end on 3 excluding 13
    if eval (a [8]) ==  0:
        day = a[9]+'rd'
    else:
        if eval (a[8:10]) != 11:
            day = a [8:10]+'rd'
elif eval (a [9]) != 1 and eval (a [9]) != 2 and eval (a [9]) != 3 or eval (a [8:10]) ==  11 or eval (a [8:10]) ==  12 or eval (a [8:10]) ==  13: # for the days that do not end on 1, 2, or 3 as well as for the 11th, 12th and 13th
    if eval (a[8]) == 0:
        day = a [9]+'th'
    elif eval(a[8,]) != 0:
        day = a[8:10]+'th'

if int(a[5:7]) == 1:
        month = 'January'
if int(a[5:7]) == 2:
        month = 'February'
if int(a[5:7]) == 3:
        month = 'March'
if int(a[5:7]) == 4:
        month = 'April'
if int(a[5:7]) == 5:
        month = 'May'
if int(a[5:7]) == 6:
        month = 'June'
if int(a[5:7]) == 7:
        month = 'July'
if int(a[5:7]) == 8:
        month = 'August'
if int(a[5:7]) == 9:
        month = 'September'
if int(a[5:7]) == 10:
        month = 'October'
if int(a[5:7]) == 11:
        month = 'November'
if int(a[5:7]) == 12:
        month = 'December'

# print year format
if eval (a[2]) == 0:
    year = '0'+a[3]
elif eval (a[2]) != 0:
    year = int(a[2:4])
        
print (time+' ', am_pm, " on the ", day, " of ", month , " \'", year, sep='')