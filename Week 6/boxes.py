# A program to create hollow boxes of stars
# Mwansa Ng'andu
# 09 April 2022

def print_square (): 
    '''
    returns a string containing a 5x5 box.
    '''
    topline = '* '*4 + '*'
    middlelines = '*' +  ' '*7 + '*' + '\n'
    bottomline = topline
    return topline + '\n' + middlelines*3 + bottomline

def print_rectangle (width, height): 
    '''
    prints a box on the screen with given width and height
    '''
    topline = '* '* width
    middlelines = '*' + ' '*(width*2-3) + '*' + '\n'
    bottomline = topline
    box = topline + '\n' + middlelines*(height-2) + bottomline
    print (box)
    
def get_rectangle (width, height): 
    '''
    returns a string containing a box with given width and height
    '''
    topline = '* '*width
    middlelines = '*' + ' '*(width*2-3) + '*' + '\n'
    bottomline = topline
    return topline + '\n' + middlelines*(height-2) + bottomline
def main():
    print (print_square())
    print (print_rectangle(6,4))
    print (get_rectangle(2, 2))  

if __name__=="__main__":
    main()