# A recursive that can be used to determine if a given pattern matches a given word
# Mwansa Ng'andu
# 27 April 2022

def match (pattern, word):
    '''
    Determine if a given pattern matches a given word
    '''
    asterisk = (pattern[::-1].find('*')*-1)-1
    if len(pattern) == 0 and len(word) == 0: # Both pattern and word are completely diminished
        return True
    
    if len(pattern) > 1 and pattern[0] == '*' and len(word) == 0: # Where pattern is '*...' and word is ''  
        return False
    
    if (len(pattern) > 1 and pattern[0] == '?') or (len(pattern) != 0 and len(word) !=0 and pattern[0] == word[0]): 
        # where pattern is '?...' OR pattern and word are not completely dimished and have the same first letter
        return match (pattern[1:], word[1:]) # Start pattern and word with the letter currently in 2nd position
    
    if len(pattern) !=0 and pattern[0] == '*': # where pattern is '*...' don,t start word with the letter currently in 2nd position (keep word the same)
        if pattern[:asterisk:-1] == word[:asterisk:-1]:
            return True
        else:
            return match (pattern[1:], word) 
    return False # if no if statement applies pattern and word does not match


