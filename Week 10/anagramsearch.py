# a Python program called ‘anagramsearch.py’ that searches a file for anagrams of a given word, printing the results in alphabetical order
# Mwansa Ng'andu
# NGNMWA001
# 04 May 2022
import os.path

print ('***** Anagram Finder *****')
try:
    file = []
    myFile = open('EnglishWords.txt', 'r', encoding = 'utf-8')
    for line in myFile:
        line = line.replace('\n', '')
        words = line.split(' ')
        for term in words:
            file.append(term)
    myFile.close()
    file = ' '.join(file)
except: # shows what the program should do if it does not find the words file
    if not os.path.isfile('EnglishWords.txt'):
        print ("Sorry, could not find file 'EnglishWords.txt'.")
finally:
    if os.path.isfile('EnglishWords.txt'):
        if 'START' in file: # avoid copyright if any 
            index = file.index('START')+6
            allText = file[index::]
        else:
            allText = file
                
        allText = allText.split(' ')
        
        word = input ('Enter a word: \n')
        word = word.lower()        
        
        dct = {} # create a dictionary for letters in given word
        for letter in word:
            if letter!='':
                if letter not in dct:
                    dct[letter]=1 # add letter to dictionary
                else:
                    dct[letter] = dct[letter]+1 # incraese frequency of letter in dictionary
                    
        List = [] # create list to store anagrams
        dct_2 = {} # create a dictionary for letters in term from allText        
        for term in allText:
            term = term.lower()
            if term == word: 
                continue
            if len(term) == len (word): # only analyze terms as long as word
                for letter in term:
                    if letter!='':
                        if letter not in dct_2:
                            dct_2[letter]=1
                        else:
                            dct_2[letter] = dct_2[letter]+1 # incraese frequency of letter in dictionary  
                # if term is an anagram of word add to list and clear term dictionary
                if dct == dct_2:
                    dct_2.clear()
                    List.append(term) 
                # if term is not an anagram simply clear term dictionary
                else:
                    dct_2.clear()
        List.sort() # arrange anagrams aphabetically
        if List != []:
            print (List)        
        else:
            print ("Sorry, anagrams of '"+word+"' could not be found.")
        

