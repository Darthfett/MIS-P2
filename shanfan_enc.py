
class Sf_Entry:    #defines a coded value entry for a Shannon-Fano table
    def __init__( self):
        self.val = -1
        self.freq = 0
        self.code = ""

    def __init__( self, pval):
        self.val = pval
        self.freq = 0
        self.code = ""

    def __repr__(self):
        return '\n[val: {0} [{0:08b}b]\t| freq: {1}\t| code: {2}]'.format(self.val, self.freq, self.code)

    #use to get the code in binary format
    def getCode( self):
        return self.code

    #use to append a 1 or 0 to the code
    def appendToCode( self, val):
        oldCode = self.code
        if(self.code == ""):
            self.code = "{0}".format(val)
        else:
            self.code += "{0}".format(val)
        #print ('{0} -> {1}'.format( oldCode, self.code) )

    def incrFreq( self):
        self.freq = self.freq + 1

class LZWCode:    #defines a coded value entry for a LZW table
    def __init__( self):
        self.color = []
        self.out_code = ""

    def __init__( self, color):
        self.color = color
        self.out_code = ""
        x
    def __repr__(self):
        return '\n[color: {0} | code: {2}]'.format(self.color, self.code)


##Shannon-Fanno Coding methods below
##
def shanfan_encode( chan):
    #Start finding codes
    #find frequency
    tbl = evaluateFrequencies( chan)
    #sort table by frequency
    tbl_2 = sort(tbl, False)
    
    #division/coding
    tbl_3 = segmentTable( tbl_2)
    ##print("\n\t\t\t== Code Table ==\n")
    ##print(tbl_3)

    #encode image
    tbl_4 = encodeShannonFanno(chan, tbl_3)
    ##print("\nOutput:")
    ##print( tbl_4)
    return tbl_4, tbl_3

def shanfan_decode(chan, decTbl):
    decodedChan = ""
    buffr = ''
    for code in chan:
        buffr += str(code)
        for entry in decTbl:
            if(buffr == entry.code):
                decodedChan += str(entry.val)
                buffr = ''
                break
    return decodedChan

def encodeShannonFanno(chan, codTbl):
    codedChan = ""
    for val in chan:
        for entry in codTbl:
            if(val == entry.val):
                codedChan += entry.getCode()
                break
    return codedChan

#evaluate list of colors
def evaluateFrequencies( chan):
    v_list = []             #for tracking colors seen in 'chan'
    sf_entArr = []            #list of Color Entries. Recall that ColorEntry tracks frequency
        
    for val in chan:        #for each color listing in chan
        if( val not in v_list):
            v_list.append( val)         #track this val
            sf_ent = Sf_Entry(val)            #start new val entry
            sf_entArr.append( sf_ent)    #add val entry to list
            ##print( 'Found new val:{0}'.format( val))
        sf_entArr[ v_list.index( val)].incrFreq()    #increase frequency

    return sf_entArr

#sort list by frequency in descending order
def sort( arr, ascending):
    #quicksort
    if( len( arr) <= 1):
        return arr
    pivot = arr.pop( len( arr)//2) #get middle entry as pivot
    upper = []
    lower = []
    arrOut = []

    #print(arr)
    for sf_ent in arr:
        if(sf_ent.freq > pivot.freq):
            upper.append( sf_ent)
        else:
            lower.append( sf_ent)
    
    if(ascending):
        arrOut.extend( sort( lower, ascending))
        arrOut.append( pivot)
        arrOut.extend( sort( upper, ascending))
    else:
        arrOut.extend( sort( upper, ascending))
        arrOut.append( pivot)
        arrOut.extend( sort( lower, ascending))
        
    #print("\nIter on length {0}, done. Returning this:".format(len(arr)))
    #print (arrOut)
    return arrOut

#use list slicing here, and value as we slice
def segmentTable( tbl):

    tbl_buffer = tbl
    code_buffer = 0
    top_tbl = []
    bot_tbl = []
    allsum = 0
    topsum = 0;
    botsum = 0
    for shafa_code in tbl_buffer:
        allsum = allsum + shafa_code.freq
    ##print('========================\n\nSum of all frequencies = {0}\n'.format(allsum))    
    
    #break table into two segments with roughly equal frequency sums
    while(topsum < allsum // 2) and (len( tbl_buffer) > 0):
        buffer0 = tbl_buffer[0]
        topsum += buffer0.freq
        top_tbl.append( tbl_buffer.pop( 0))    #push Code Entry to top list
    ##    print(top_tbl)
    #do the same with bottom segment, if bottom segment 'sum < halfSumAllFrequencies'. these tables will be roughly equal
    while(botsum < allsum // 2) and (len( tbl_buffer) > 0):
        buffer1 = tbl_buffer[0] #pop another element off the list. We're nwo in lower table's half pretty much.
        botsum += buffer1.freq
        bot_tbl.append( tbl_buffer.pop( 0))    #push Code Entry to top list
        if(botsum > allsum):
            lastInd = len( top_tbl) - 1
            lastTopEntry = top_tbl[ lastInd]
            if(botsum + lastTopEntry.freq < topsum) and (botsum + lastTopEntry.freq > (allsum / 2)):
                bot_tbl.append( top_tbl.pop( lastind))
        #check if last entry from top segment plus bottom sum is greater than half the total sum.

    for entry in top_tbl:
    ##    print("\n{0} Appended 0".format( entry.printColor()))
        entry.appendToCode(0) #left shift top codes and set LSB to 0
    for entry in bot_tbl:
    ##    print("\n{0} Appended 1".format( entry.printColor()))
        entry.appendToCode(1) #left shift top codes and set LSB to 1
    
    if len(top_tbl) > 1:
        top_tbl = segmentTable( top_tbl)
    if len(bot_tbl) > 1:
        bot_tbl = segmentTable( bot_tbl)
    top_tbl.extend(bot_tbl)
    return top_tbl
    
