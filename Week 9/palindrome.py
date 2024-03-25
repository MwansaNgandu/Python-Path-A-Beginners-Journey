# A recursive function to calculate whether or not a string is a palindrome (reads the same if reversed)
# Mwansa Ng'andu
# 27 April 2022

def IsPalindrome (string):
    '''
    Calculate whether or not a string is a palindrome
    '''
    if len(string) < 2: # Palindrome because letter is the element in string
        return 'Palindrome!'
    if string[0] != string[-1]: # Compare first and last letter of string
        return 'Not a palindrome!'
    return IsPalindrome(string[1:-1])    

def main ():
    string = str (input ('Enter a string:\n'))
    print (IsPalindrome (string))

if __name__=='__main__':
    main ()