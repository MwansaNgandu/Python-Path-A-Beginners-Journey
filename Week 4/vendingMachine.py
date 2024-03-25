# A program to simulate a vending machine and calculate change based on the amount paid
# Mwansa Ng'andu
# NGNMWA001
# 02 March 2022

# Obtain cost from user
cost = eval(input ("Enter the cost (in cents):\n")) 

# Obtain deposited by user
total_money_deposited = 0
while total_money_deposited < cost:
    money_deposited = eval(input ("Deposit a coin or note (in cents):\n"))
    total_money_deposited += money_deposited
  
change = total_money_deposited - cost

rands = change // 100 # Use integer division to obtain the rand amount
cents = change % 100 # Use mode to obtain the cents amount

if change != 0:
    print ("Your change is:") 
    
# Determine the rand amount distribution 
if change >= 100 and change < 200 and change != 0: # Execute when the change is greater than or equal to 100c but less than 200c
    no_R_coins = change//100
    print (no_R_coins, 'x R1')
    
if change >= 200 and change < 500 and change != 0: # Execute when the change is greater than or equal to 200c but less than 500c
    no_R_coins = change//200
    remainder = rands%2
    print (no_R_coins, 'x R2')
    if remainder > 0:
        print (remainder, 'x R1')
    
if change >= 500 and change != 0: # Execute when the change is greater than or equal to 500c but less than 500c
    no_R_coins = change//500
    remainder = rands%5
    print (no_R_coins, 'x R5')
    if remainder == 4:
        print ('2 x R2')
    elif remainder == 3:
        print ('1 x R2')
        print ('1 x R1')
    elif remainder == 2:
        print ('1 x R2')
    elif remainder == 1:
        print ('1 x R1')
        
# Determine the cents amount distribution 
if cents >= 5 and cents < 10 and cents != 0:
    no_c_coins = cents//5
    remainder = rands%5
    print (no_c_coins, 'x 5c')  
    
elif cents >= 10 and cents < 20 and cents != 0:
    no_c_coins = cents//10
    remainder = cents%10
    print (no_c_coins, 'x 10c')  
    if remainder >0:
        print ("1 x 5c")
        
elif cents >= 20 and cents < 50 and cents != 0:
    no_c_coins = cents//20
    remainder = cents%20
    print (no_c_coins, 'x 20c')
    if remainder >0:
        print ("1 x 5c")        
        
elif cents >= 50 and cents < 100 and cents != 0:
    no_c_coins = cents//50 
    remainder = cents%50
    print (no_c_coins, 'x 50c')
    
    if remainder >0:
        if remainder == 45:
            print ('2 x 20c')
            print ('1 x 5c')
        if remainder == 40:
            print ('2 x 20c')       
        if remainder == 35:
            print ('1 x 20c')   
            print ('1 x 10c')
            print ('1 x 5c')
        if remainder == 30:
            print ('1 x 20c')
            print ('1 x 10c')                
        if remainder == 25:
            print ('1 x 20c')
            print ('1 x 5c')
        if remainder == 20:
            print ('1 x 20c')
        if remainder == 15: 
            print ('1 x 10c')
            print ('1 x 5c')
        if remainder == 10:
            print ('1 x 10c')
        if remainder == 5:
            print ('1 x 5c')