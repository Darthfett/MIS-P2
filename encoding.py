import collections

ENCODING_SCHEME_NONE = 1
ENCODING_SCHEME_VARLEN = 2
ENCODING_SCHEME_DICT = 3

DEBUG_VERBOSE = True

class ShaFaCode:
    def __init__( self):
        self.color = list(0,0,0)
        self.freq = 0
        self.code = 0

    def __init__( self, color):
        self.color = color
        self.freq = 0
        self.code = 0
    def __repr__(self):
        return '\n[color: {0} | freq: {1} | code: {2}]'.format(self.color, self.freq, self.code)

    def setColors( self, r, g, b):
        self.color = (r, g, b)

    def getColor( self):
        return self.color

    #use to get the code in binary format
    def code( self):
        return '{0:08b}'.format(self.code)

    #use to append a 1 or 0 to the code
    def appendToCode( self, val):
        self.code = self.code << 1 | val

    def incrFreq( self):
        self.freq = self.freq + 1


#(Task 5): Given ???, perform the following encoding schemes:
#    - Encoding Option 1: No encoding
#    - Encoding Option 2: Variable-length encoding with Shanno-Fano coding
#    - Encoding Option 3: Dictionary encoding with LZW coding (for a given dictionary bit length)

def encode( img, opcode):
    if( opcode == ENCODING_SCHEME_DICT):
        encode_shannonFano(img)

    #raise NotImplementedError("TODO: Implement encoding functionality")

#evaluate list of colors
def evaluateFrequencies( img):
    colList = []             #for tracking colors seen in 'img'
    sfcodeArr = list()            #list of Color Entries. Recall that ColorEntry tracks frequency
    if( len(img) == 3):
        img = zip(img)        #set IMG to be in pixel format. Expecting it to be a tuple/list of three tuple
        print('zipped array parameter \'img\'')
        if( len(img) <= 3):
            raise IndexError('Parameter (img) was of length 3 or less, even after zipping', "length", len(img))

    for color in img:        #for each color listing in img
        if( color not in colList):
            colList.append( color)         #track this color
            sfcode = ShaFaCode(color)            #start new color entry
            sfcodeArr.append( sfcode)    #add color entry to list
            print( 'Found new color, (r:{0}, g:{1}, b:{2})'.format(sfcodeArr[len(sfcodeArr) - 1].color[0], color[1], color[2]))
        sfcodeArr[ colList.index( color)].incrFreq()    #increase frequency

    return sort(sfcodeArr)

#sort list by frequency in descending order
def sort( arr):
    #quicksort
    if( len( arr) <= 1):
        return arr
    pivot = arr.pop( len( arr)//2) #get middle entry as pivot
    upper = list()
    lower = list()
    arrOut = list()

    print(arr)
    for sfcode in arr:
        print ("Sorting")
        if(sfcode.freq > pivot.freq):
            upper.append( sfcode)
        else:
            lower.append( sfcode)

    arrOut.extend( sort( upper))
    arrOut.append( pivot)
    arrOut.extend( sort( lower))
    print("\nIter on length {0}, done. Returning this:".format(len(arr)))
    print (arrOut)
    return arrOut

#use list slicing here
def segment(freqArray, start, end ):

    return freqArray

def encode_shannonFano(img):
    colors = list()    #list of colors
    segments = list()    #list of segmen

    #Evaluate for frequency of colors found inside img
        #add them to colors as a tuple, set freq and code to 0 for the tuple.

    #Sort frequencies

    #Start finding codes

        #division
        #break table into two segments with roughly equal frequency sums
            #add color freq to top segment sum until 'sum >= halfSumAllFrequencies',
            #do the same with bottom segment, if bottom segment 'sum < halfSumAllFrequencies', check if last entry from top segment plus bottom sum is greater than half the total sum.
                #repeat until true and while new sum is not greater than (newest) top segment's sum
            #left shift code of every entry, and set top segments LSB's to 0, bottom segments LSB's to 1
