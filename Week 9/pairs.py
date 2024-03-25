# A recursive function to count the number of pairs of consecutive characters in a string
# Mwansa Ng'andu
# 27 April 2022

def count_pairs (string):
    '''
    Count the number of pairs of consecutive characters in a string
    '''
    if len (string) <= 1: # Base case 
        return 0
    elif string[0] == string[1]:# Count consecutive identical characters of string
        return 1 + count_pairs (string[2:])
    else:
        return count_pairs (string[1:]) # Else restart string from 2nd current character
    

def main ():
    message = str (input ("Enter a message:\n"))
    count = count_pairs (message)
    print ("Number of pairs:", count)

if __name__=='__main__':
    main ()