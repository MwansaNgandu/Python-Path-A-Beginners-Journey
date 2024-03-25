# A recursive functions to find all palindromic primes between two integers N, M, supplied as input
# Mwansa Ng'andu
# 27 April 2022

import sys
sys.setrecursionlimit (30000)

N = int (input ("Enter the starting point N:\n"))
M = int (input ("Enter the ending point M:\n"))
print ("The palindromic primes are:")
        
def is_prime(N, M, a=2):
    '''
    find all primes numbers between two integers N, M, supplied as input
    '''
    if N == M: # reached stop number
        return
    if (N <= 2): # first prime number is 2
        if (N == 2):
            is_palindrome(N)
            return is_prime(N+1, M, a=2) 
        else:
            return is_prime(N+1, M, a=2)    
    if int(str(N)[len(str(N))-1]) == 2 or int(str(N)[len(str(N))-1]) == 4 or int(str(N)[len(str(N))-1]) == 5 or int(str(N)[len(str(N))-1]) == 6 or int(str(N)[len(str(N))-1]) == 8 or int(str(N)[len(str(N))-1]) == 0: # exclude numbers that end on 2, 4, 6, 8, 0 and 5
        return is_prime(N+1, M, a=2)
    if (N % a == 0): # if number is divisable by any number other than itsself, not a prime numbe
        return is_prime (N+1, M, a=2)
    if (a * a > N):
        is_palindrome(N)
        return is_prime(N+1, M, a=2) 
     
    return is_prime(N, M, a + 1) # check for next divisor
            
def is_palindrome(num):
    '''
    find all palindromes of N supplied by is_prime
    '''
    if str(num) == str(num)[::-1]: # check if prime number is a palindrome
        print (num)