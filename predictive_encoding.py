
def predict_encoding(im, choice):
    """
    (Task 3):     Parameters are a python image object and an integer representing the choice for prediction algorithm, this function
    returns a pixel list (list of 3-tuples of r,g,b values).
    It does this by getting the pixel list, separating it into 3 color channels, then for each color channel calling the
    prediction algorithm.  Then it zips the color channels back together and returns

    - PC Option 1: No PC (use original values).
    - PC Option 2: Predictive encoding with the predictor A.
    - PC Option 3: Predictive encoding with the predictor B.
    - PC Option 4: Predictive encoding with the predictor C.
    - PC Option 5: Predictive encoding with the predictor (A+B+C) / 3.
    - PC Option 6: Predictive encoding with the predictor A + (B - C) = B + (A - C).
    - PC Option 7: Predictive encoding with the predictor (A+B) / 2.
    - PC Option 8: Predictive encoding with the predictor:
        * if B - C > 0 and A - C > 0 then C + sqrt((B - C)^2 + (A - C)^2),
        * else if B - C < 0 and A - C < 0 then C - sqrt((B - C)^2 + (A - C)^2,
        * else (A+B) / 2.

    """
    pixList = list(im.getdata())
    r,g,b = zip(*pixList)
    height, width = im.size
    r = predict(r, width, height, choice)
    g = predict(g, width, height, choice)
    b = predict(b, width, height, choice)
    z = zip (r,g,b)
    #print z # for testing
    return z


def predict (r, width, height, choice):
    '''
    given a list of values of 1 channel of an image, the width and height of the image, and the choice of prediction algorithm,
    return the list of values in this channel with the prediction algorithm applied.
    '''
    table = [[0 for i in range(height)]for j in range (width)] 
    # Creates a table with (height) rows and (width) columns with all values initialized to 0

    for d1 in range (height):
        table[d1][0] = r[d1*width]
    for d2 in range (width):
            table [0][d2] = r[d2] # Now table is fully initialized - It has all of the top and left values from 'r'.
    
    #There's probably a more elegant way to do this. Series of elifs in place of a switch statement
    #to find out what choice is
    if (choice == 1):
        return r
    elif (choice == 2):
        for row in range(1, height):
            for column in range(1, width):
                table[row][column] = table[row][column-1] 
                
    elif (choice == 3):
        for row in range (1, height):
            for column in range (1, width):
                table [row][column] = table[row-1][column]
                
    elif (choice == 4):
        for row in range (1, height):
            for column in range (1, width):
                table [row][column] = table[row-1, column-1]
    
    elif (choice == 5):
        for row in range (1, height):
            for column in range (1, width):
                table [row][column] = (table[row][column-1]+table[row-1][column]+table[row-1][column-1])/3
            
    elif (choice == 6):
        for row in range (1, height):
            for column in range (1, width):
                table [row][column] = (table[row][column-1])+(table[row-1][column]-table[row-1][column-1])
                
    elif (choice == 7):
        for row in range (1, height):
            for column in range (1, width):
                table[row][column] = (table[row][column-1]+table[row-1][column])/2
                
    elif (choice == 8):
        for row in range (1, height):
            for column in range (1, width):
                a,b,c = table[row,column-1],table[row-1][column],table[row-1,column-1]
                if ((b-c)>0 and (a-c)>0):
                    table[row,column]= c + sqrt((b-c)*(b-c)+(a-c)*(a-c))
                elif ((b-c)<0 and (a-c)<0):
                    table[row,column] = c - sqrt((b-c)*(b-c)+(a-c)*(a-c))
                else:
                    table[row,column] = (a+b)/2
    
    else:
        #Haven't decided how to handle bad input
        #error: bad input
        print "error"##
        
    return_list = []
    for row in range (0, height): #Go through table in order, and add all values to return_list
        for column in range (0, width):
            n = table[row][column]
            return_list.append(n)
    return return_list
