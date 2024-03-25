# A program to extract useful data from a raw data stream obtained from a sensor
# Mwansa Ng'andu
# 09 April 2022

# BEGIN 25.3_0:138.6E,44.0N DIRDAM END

def get_block(data):
    """the get_block function extracts the sub string starting with ‘BEGIN’ and ending with ‘END’
    """
    start = data.find('BEGIN')
    end = data.find('END')+2
    data_input = data[start:end+1] # remove what comes before and after BEGIN and End respectively
    return data_input

def location(block):
    """the location function returns the location component in title case
    """
    global end
    global position
    south = block.find('S')
    north = block[5::].find('N')+5
    if not south > 0:
        position = north 
    else:
        position = south
    return block[-5:position+1:-1].title()

def y_coordinate(block):
    """the y_coordinate function returns the y coordinate component as a string
    """
    global comma
    south = block.find('S')
    north = block[5::].find('N')+5
    if not south > 0:
        position = north 
    else:
        position = south    
    comma = block.find(',')    
    return block[comma+1:position+1]

def x_coordinate(block):
    """the x_coordinate function returns the x coordinate component as a string
    """
    global colon
    comma = block.find(',')
    colon = block.find(':')    
    return block[colon+1:comma]

def temperature(block):
    """the temperature function returns the temperature component as a real number value
    """
    global underscore
    underscore = block.find('_')
    return eval(block[6:underscore])

def pressure(block):
    """the pressure function returns the pressure component as a real number value
    """
    colon = block.find(':')  
    underscore = block.find('_')
    return eval(block[underscore+1:colon])

def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))

if __name__=='__main__':
    main()
