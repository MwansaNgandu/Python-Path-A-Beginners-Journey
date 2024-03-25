# A program to search a file for sets of words that are anagrams of each other
# Mwansa Ng'andu
# NGNMWA001
# 04 May 2022

def create_dictionary(word):
    '''
    create a dictionary for letters in given word
    '''
    word_dictionary = dict()
    for letter in word:
        word_dictionary[letter] = word_dictionary.get(letter,0) + 1
    return word_dictionary

def search(List, word_dictionary):
    '''
    search List and return anagrams for given words
    '''
    combined_anagrams = [] # list of found anagrams
    for word in List:
        if word in combined_anagrams: # don't analyze words already recognized as anagrams
            continue
        else:
            anagrams = []
            term_dictionary={}
            for term in List:
                for letter in term:
                    if letter not in term_dictionary:
                        term_dictionary[letter]=1 # add letter to dictionary
                    else:
                        term_dictionary[letter] = term_dictionary[letter]+1 # incraese frequency of letter in dictionary  
                # if term is an anagram of word add to list and clear term dictionary
                if word_dictionary == term_dictionary:
                    anagrams.append(term)
                    term_dictionary.clear()
                # if term is not an anagram simply clear term dictionary
                else:
                    term_dictionary.clear()
            if len(anagrams) > 1: # add anagrams to combined anagrams 
                combined_anagrams += anagrams
                combined_anagrams.sort() # put list in alphabetical order
                return combined_anagrams
            else:
                return []

def main():
    print ('***** Anagram Set Search *****')
    length = eval(input ('Enter word length:\n'))
    print ('Searching...')
    
    filename = input ('Enter file name:\n')
    myFile = open('EnglishWords.txt', 'r', encoding = 'utf-8')
    file = myFile.read()
    myFile.close()
    
    if 'START' in file: # avoid copyright if any 
        index = file.index('START')+6
        allText = file[index::]
    else:
        allText = file
            
    allText = allText.replace('\n', ' ') # remove unwanted characters
    allText = allText.split(' ')    
    
    print ('Writing results...')
    
    List = []
    for term in allText: 
        term = term.lower()
        if len(term) == length:
            if term not in List:
                List.append(term)
                
    f = open (filename, 'w') # create new file
    checker = []
    List.sort()
    for word in List:
        if word not in checker: 
            word_dictionary = create_dictionary(word)
            anagrams = search(List, word_dictionary)
            if anagrams != []:
                checker += anagrams
                print (anagrams)
                f.writelines("{}\n".format(anagrams)) # overwrite file with new code
    f.close()    
if __name__ == '__main__':
    main()