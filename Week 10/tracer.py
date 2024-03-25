# A program that may be used to assist with debugging Python programs
# Mwansa Ng'andu
# NGNMWA001
# 04 May 2022

def search_def (word, file): 
    '''
    search for 'def' line and add DEBUG line following it
    '''
    for line in file:
        index = file.index(line)+1 # index for debug line to be added
        line = line.split(' ')
        for term in line:
            if term == word: # to find 'def...' line
                length = len(line)
                if '(' in line[1]:
                    bracket = line[1].find('(')
                    function = line[1][:bracket:]
                    file.insert(index,'    """DEBUG"""'+";print('"+function+"')\n") # insert debug line into file
                    break
                else:
                    file.insert(index,'    """DEBUG"""'+";print('"+''.join(line[1:length-1:])+"')\n") # insert debug line into file
                    break
        # if found: break  # remove if want for more than just the first occurence
    return file

def search_remove (word, file): 
    ''' 
    remove all debug lines added
    '''
    for line in file:
        index = file.index(line)+1 # index of debug lines
        line = line.split(' ')
        for term in line:  
            if term == word: # to find 'def...' line
                del file[index] # remove debug lines into file
    file = file[1::] # remove first debug line into file
    return file    

print("***** Program Trace Utility *****")
program = input("Enter the name of the program file: ")
myFile = open(program,"r")

file = myFile.readlines() # store file as list of strings
myFile.close() 

if '"""DEBUG"""\n' not in file[0]: # identify that file needs DEBUG lines to be added
    print ('Inserting...Done')
    new_file = search_def ('def', file)
    new_file.insert(0, '"""DEBUG"""\n')
    ''.join(new_file)
else:
    if '"""DEBUG"""\n' in file[0]: # identify that file needs DEBUG lines to be removed
        new_file = search_remove ('def', file)
        ''.join(new_file)
        print ('Program contains trace statements')
        print ('Removing...Done') 

f = open (program, 'w') # clear same py file
f.writelines(new_file) # overwrite file with new code
f.close()