import math
def quantize(color_channels, N=((None,)*3)): # Default values of None to indicate no quantization.
    """
    (Task 2): Given three channels c1, c2, c3 of an image, and three numbers n1, n2, n3,
    uniformly quantize the channels into n1, n2, n3 bins respectively.
    """
    c1, c2, c3 = color_channels
    n1, n2, n3 = N

    c1New = calcquant(c1, n1)
    c2New = calcquant(c2, n2)
    c3New = calcquant(c3, n3)

    return c1New, c2New, c3New

def calcquant(channel, numBins):
    values = range(0, 256)
    #Since we are assuming uniform distribution across 256 color instances,
    #We simply need to divide 256 by the requested bin size to find the
    #range to be represented by the median instance

    #bins is actually just a list of key:value pairs that maps the actual error value
    #as a key to the new quantized value

    if numBins is None:
        return channel

    binsize = math.floor(len(values)/numBins)
    offset = math.floor(binsize/2)

    bins = dict()
    lowerbound = 0
    key = 0
    median = lowerbound + offset
    upperbound = lowerbound + binsize
    while(upperbound < len(range(0, 256))):
        while(lowerbound < upperbound):
            bins[key] = median
            key = key + 1
            lowerbound = lowerbound + 1
        upperbound = upperbound + binsize
        median = lowerbound + offset

    quantized = list()
    #The original values of the channel, as received by method, act as keys
    #for retrieving the new representative value, which is the median of the bin
    for i, val in enumerate(channel):
        quantized.append(bins[val])