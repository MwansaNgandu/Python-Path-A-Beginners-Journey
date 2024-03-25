# A recursive function that can be used to determine if a given pattern matches a given word
# Mwansa Ng'andu
# 27 April 2022

def match (pattern, word):
    '''
    A recursive function that can be used to determine if a given pattern matches a given word
    '''
    if(len(pattern) != len(word)): # Pattern and Word are not the same length
        return False   
    
    elif len(word) == len(pattern) and len(pattern) == 0: # Both pattern and word are completely diminished
        return True
    
    else:
        if(pattern[0] != '?' and pattern[0] != word[0]): # New start letter of pattern is not '?' and is not the same as start letter of word
            return False
        else:
            return match(pattern[1:], word[1:]) # Start pattern and word with the letter currently in 2nd position
            