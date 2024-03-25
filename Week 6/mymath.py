# A program to create 2 required functions
# Mwansa Ng'andu
# 09 April 2022

def get_integer(s): 
   '''
   accepts an integer, s, from the user
   '''
   global n
   if s== 'n':
      n = eval(input ("Enter n:\n"))

   elif s == 'k':
      k = input ("Enter k:\n")
   
   elif s!= 'n' and s!= 'k':
      input ("Enter number:\n")
   
def calc_factorial(c):
   '''iteratively calculates the factorial of an integer n
   '''
   if c == 0:
      return 1
   else:
      return c*calc_factorial(c-1)
def main ():        
   print (get_integer(3))
   print (calc_factorial (4))
 
if __name__=='__main__':
   main()