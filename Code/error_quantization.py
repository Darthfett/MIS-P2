from __future__ import division

import math

from byte_packer import int_seq_to_bytearray

def error_quantize(channel, num_bins, maxval):
    if not num_bins:
        return channel

    # Get amount covered by each bin
    bin_size = int(math.ceil(maxval * 2 / num_bins))

    # Get bin for each value in channel
    bin_vals = [int((i + maxval) / bin_size) for i in channel]

    return int_seq_to_bytearray(bin_vals, num_bins-1)

def error_quantization(image, error, maxvals, m=None):
    """
    (Task 4): Given image as a list of values post-predictive coding, and m,
    perform uniform OR non-uniform quantization of the error into m bins.
    """

    if m is None:
        e1 = int_seq_to_bytearray(error[0], maxvals[0])
        e2 = int_seq_to_bytearray(error[1], maxvals[1])
        e3 = int_seq_to_bytearray(error[2], maxvals[2])
        return e1, e2, e3

    e1, e2, e3 = error

    e1New = error_quantize(e1, m, maxvals[0])
    e2New = error_quantize(e2, m, maxvals[1])
    e3New = error_quantize(e3, m, maxvals[2])

    return e1New, e2New, e3New
    #error quantization principle:  get the first value, and all following
    #information is the difference between the original and the predicted signal
    #predictive coding is done in previous task, so this task needs to
    #perform the following:
    #    1)  calculate bin range (m = user input = # of bins)
    #           !!!  error value range:  [-255...0...255] = 511 possible values
    #    2)  if difference between bin's lower & upper,
    #           assign new difference value that is median between the two

def calcquant_old(error, m):
    values = range(-255, 256)

    #bins is actually just a list of key:value pairs that maps the actual error value
    #as a key to the new quantized value
    binsize = math.floor(len(values)/m)
    offset = math.floor(binsize/2)

    bins = dict()
    lowerbound = -255
    key = -255
    median = lowerbound + offset
    upperbound = lowerbound + binsize
    while(upperbound + binsize <= len(values)):
        while(lowerbound < upperbound):
            bins[key] = median
            #print key, " :  ", bins[key]
            key = key + 1
            lowerbound = lowerbound + 1
            #print "Median is ", median, "  lowerbound is  ", lowerbound, "  upperbound is ", upperbound
        if(upperbound + binsize <= len(values)):
            upperbound = upperbound + binsize
            median = lowerbound + offset

    upperbound = len(values)
    offset = (upperbound - lowerbound)/2
    median = lowerbound + offset

    while (lowerbound < upperbound):
        bins[key] = median
        key = key + 1
        lowerbound = lowerbound + 1
    #iterate through image, and replace error values with quantized values
    #for speed, search for matching bin with binary search
    #needs to called recursively
    errorQuantized = list()
    for i, pixel in enumerate(error):
        errorQuantized.append(bins[pixel])  #bins[pixel] returns value, which is new
        #error val and is placed in new list

    return errorQuantized
