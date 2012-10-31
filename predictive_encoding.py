from math import sqrt
from PIL import Image


def reconstruct_image(r,g,b,width,height,choice):
    '''
    Parameters are same as predict_encoding, but the 3 channels are those to which the predictor has already been applied.
    This returns a tupel representing the pixels of the image reconstructed using the prediction algorithm and the 
    error values stored in r, g, and b
    '''
    r_re = reconstruct(r, width, height, choice)
    g_re = reconstruct(g, width, height, choice)
    b_re = reconstruct(b, width, height, choice)
    z_re = zip(r_re, g_re, b_re)
    return z_re
def predict_encoding(r, g, b, width, height, choice):
    '''
    Parameters are 3 lists of values representing the 3 channels of an image, the width and height of the original image,
    and an integer representing the choice for prediction algorithm. This function returns a pixel list 
    (list of 3-tuples of r,g,b values).
    It does this by getting the pixel list, separating it into 3 color channels, then for each color channel calling the
    prediction algorithm.  Then it zips the color channels back together and returns
    
    Don't know whether to return predicted image, or list of error values calculated while predicting. I think the latter,
    though.
    '''

    '''pixList = list(im.getdata())
    r,g,b = zip(*pixList)
    height, width = im.size'''
    r_errors, r_predicted = predict(r, width, height, choice)
    g_errors, g_predicted = predict(g, width, height, choice)
    b_errors, b_predicted = predict(b, width, height, choice)
    z_new = zip (r_errors,g_errors,b_errors)
    return z_new
    ''' r_new = predict(r, width, height, choice)
    g_new = predict(g, width, height, choice)
    b_new = predict(b, width, height, choice)'''
    #print r_new
    
    '''
    the following is if errors are supposed to be calculated at the end of predictions:
    
    r_errors = []
    g_errors = []
    b_errors = []
    length = len(r)
    for i in range (length):
        r_errors.append(r_new[i]-r[i])
        g_errors.append(g_new[i]-g[i])
        b_errors.append(b_new[i]-b[i])
    '''
    #print "r_errors:", r_errors
    #print "g_new:", g_new
    #print "b_new:", b_new
    #print "r_new:", r_new
    #print "r: ", r
    
    


def predict (r, width, height, choice):
    '''
    given a list (tuple?) of values of 1 channel of an image, the width and height of the image, and the choice of prediction algorithm,
    return the list of values in this channel with the prediction algorithm applied.
    '''
    table = [[0 for i in range(height)]for j in range (width)]
    table_o = [[0 for i in range(height)]for j in range (width)]
    table_e = [[0 for i in range(height)]for j in range (width)]
    # Creates 2 tables with (height) rows and (width) columns with all values initialized to 0
    # table_o (original) will hold original values from the list given
    # table_e (errors) will hold the error values. 

    for d1 in range (height):
        table[d1][0] = r[d1*width]
    for d2 in range (width):
            table [0][d2] = r[d2] # Now table is fully initialized - It has all of the top and left values from 'r'.
     
    for d1 in range (height):
        table_e[d1][0] = r[d1*width]
    for d2 in range (width):
            table_e [0][d2] = r[d2]
            # the first value of every row and column will match the originals, the other values will be
            # error (predicted - original)
            
    for d1 in range (height):
        for d2 in range (width):
            table_o[d1][d2] = r[width*d1 + d2]# now table_o has all values from 'r'.
    
    
    #print table
            
    #There's probably a more elegant way to do this. series of elifs in place of a switch statement
    #to find out what choice is
    if (choice == 1):
        return r,r
    elif (choice == 2):
        for row in range(1, height):
            for column in range(1, width):
                #table[row][column] = table[row][column-1]# if supposed to use prev. predicted values as predictors
                table[row][column] = table_o[row][column-1] # if supposed to use original values as predictors
                table_e[row][column]= table[row][column]-table_o[row][column]
                
    elif (choice == 3):
        for row in range (1, height):
            for column in range (1, width):
                #table [row][column] = table[row-1][column]
                table [row][column] = table_o[row-1][column]
                table_e[row][column]= table[row][column]-table_o[row][column]
                
    elif (choice == 4):
        for row in range (1, height):
            for column in range (1, width):
                #table [row][column] = table[row-1, column-1]
                table [row][column] = table_o[row-1][column-1]
                table_e[row][column]= table[row][column]-table_o[row][column]
    
    elif (choice == 5):
        for row in range (1, height):
            for column in range (1, width):
                #table [row][column] = (table[row][column-1]+table[row-1][column]+table[row-1][column-1])/3
                table [row][column] = (table_o[row][column-1]+table_o[row-1][column]+table_o[row-1][column-1])/3
                table_e[row][column]= table[row][column]-table_o[row][column]
            
    elif (choice == 6):
        for row in range (1, height):
            for column in range (1, width):
                #table [row][column] = (table[row][column-1])+(table[row-1][column]-table[row-1][column-1])
                table [row][column] = (table_o[row][column-1])+(table_o[row-1][column]-table_o[row-1][column-1])
                table_e[row][column]= table[row][column]-table_o[row][column]
                
    elif (choice == 7):
        for row in range (1, height):
            for column in range (1, width):
                #table[row][column] = (table[row][column-1]+table[row-1][column])/2
                table[row][column] = (table_o[row][column-1]+table_o[row-1][column])/2
                table_e[row][column]= table[row][column]-table_o[row][column]
                
    elif (choice == 8):
        for row in range (1, height):
            for column in range (1, width):
                #a,b,c = table[row][column-1],table[row-1][column],table[row-1][column-1]
                a,b,c = table_o[row][column-1],table_o[row-1][column],table_o[row-1][column-1]
                if ((b-c)>0 and (a-c)>0):
                    table[row][column]= c + int(sqrt((b-c)*(b-c)+(a-c)*(a-c)))
                    table_e[row][column]= table[row][column]-table_o[row][column]
                elif ((b-c)<0 and (a-c)<0):
                    table[row][column] = c - int(sqrt((b-c)*(b-c)+(a-c)*(a-c)))
                    table_e[row][column]= table[row][column]-table_o[row][column]
                else:
                    table[row][column] = (a+b)/2
                    table_e[row][column]= table[row][column]-table_o[row][column]
    
    else:
        #Haven't decided how to handle bad input
        #error: bad input
        print "error"##
        
    return_list_predicted = []
    return_list_errors = []
    for row in range (0, height): #Go through table in order, and add all values to return_list
        for column in range (0, width):
            n = table[row][column]
            return_list_predicted.append(n)

    for row in range (0, height): #Go through table in order, and add all values to return_list
        for column in range (0, width):
            n = table_e[row][column]
            return_list_errors.append(n)
    
    return (return_list_errors, return_list_predicted)
    #return (return_list_predicted)
    
def reconstruct (r, width, height, choice):

    table = [[0 for i in range(height)]for j in range (width)]
    # Creates a table with (height) rows and (width) columns with all values initialized to 0
            
    for d1 in range (height):
        for d2 in range (width):
            table[d1][d2] = r[width*d1 + d2]# now table has all values from 'r'.
            
    #series of elifs in place of a switch statement to find out what choice is
    if (choice == 1): # Check functionality here
        return r
    elif (choice == 2):
        for row in range(1, height):
            for column in range(1, width):
                table[row][column] = table[row][column-1]-table[row][column]
                # Makes prediction then accounts for error stored in table slot about to be written to
                
    elif (choice == 3):
        for row in range (1, height):
            for column in range (1, width):
                table [row][column] = table[row-1][column]-table[row][column]
                
    elif (choice == 4):
        for row in range (1, height):
            for column in range (1, width):
                table [row][column] = table[row-1][column-1]-table[row][column]
    
    elif (choice == 5):
        for row in range (1, height):
            for column in range (1, width):
                table [row][column] = (table[row][column-1]+table[row-1][column]+table[row-1][column-1])/3-table[row][column]
            
    elif (choice == 6):
        for row in range (1, height):
            for column in range (1, width):
                table [row][column] = (table[row][column-1])+(table[row-1][column]-table[row-1][column-1])-table[row][column]
                
    elif (choice == 7):
        for row in range (1, height):
            for column in range (1, width):
                table[row][column] = (table[row][column-1]+table[row-1][column])/2-table[row][column]
                
    elif (choice == 8):
        for row in range (1, height):
            for column in range (1, width):
                a,b,c = table[row][column-1],table[row-1][column],table[row-1][column-1]
                if ((b-c)>0 and (a-c)>0):
                    table[row][column]= c + int(sqrt((b-c)*(b-c)+(a-c)*(a-c)))-table[row][column]
                elif ((b-c)<0 and (a-c)<0):
                    table[row][column] = c - int(sqrt((b-c)*(b-c)+(a-c)*(a-c)))-table[row][column]
                else:
                    table[row][column] = (a+b)/2 - table[row][column]
    
    else:
        #Haven't decided how to handle bad input
        #error: bad input
        print "error"##
        
    return_list = []
    for row in range (0, height): #Go through table in order, and add all values to return_list
        for column in range (0, width):
            n = table[row][column]
            return_list.append(n)
    
    return (return_list)

'''
##Testing:
im = Image.open('blue_gradient.jpg')
pixList = list(im.getdata())
r,g,b = zip(*pixList)
height, width = im.size
t1 = (1,2,3,4,5,6,7,8,9)
t2 = (9,8,7,6,5,4,3,2,1)
t3 = (7,8,9,4,5,6,1,2,3)

#new_list = predict_encoding(r, g, b, width, height, 8)
new_list = predict_encoding(t1,t2,t3,3,3,7)
t1,t2,t3 = zip(*new_list)
print t1,t2,t3
final_list = reconstruct_image(t1,t2,t3,3,3,7)
t1,t2,t3 = zip(*final_list)
print t1,t2,t3
'''

#