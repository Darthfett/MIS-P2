import math
def quantize(color_channels, N=((None,)*3)): # Default values of None to indicate no quantization.
    """
    (Task 2): Given three channels c1, c2, c3 of an image, and three numbers n1, n2, n3,
    uniformly quantize the channels into n1, n2, n3 bins respectively.
    """
    c1, c2, c3 = color_channels
    n1, n2, n3 = N

    values = range(0, 255)    
    #Since we are assuming uniform distribution across 256 color instances,
    #We simply need to divide 256 by the requested bin size to find the
    #range to be represented by the median instance

    range1 = math.floor(256/n1)
    range2 = math.floor(256/n2)
    range3 = math.floor(256/n3)

    #ranges of values to be represented by the same value are grouped together
    c1Ranges = [values[x:x+range1] for x in xrange(0, len(values), n1)]
    c2Ranges = [values[x:x+range2] for x in xrange(0, len(values), n2)]
    c3Ranges = [values[x:x+range3] for x in xrange(0, len(values), n3)]

    #offsets are added to the lower bound of a range to obtain the representative
    #color value for the bin

    offset1 = math.floor(range1/2)
    offset2 = math.floor(range2/2)
    offset3 = math.floor(range3/2)

    #Map value = offset1 + LowerBound to ranges in c#Ranges


    #iterate through color_channels & replace values with new quantized values
    if not any({n1, n2, n3}):
        return c1, c2, c3

    raise NotImplementedError("TODO: Implement uniform quantization functionality")