import math
def error_quantization(m=None, img):
    """
    (Task 4): Given img as a list of values post-predictive coding, and m,
    perform uniform OR non-uniform quantization of the error into m bins.
    """
	
	#error quantization principle:  get the first value, and all following 
	#information is the difference between the original and the predicted signal
	#predictive coding is done in previous task, so this task needs to
	#perform the following:
	#	1)  calculate bin range (m = user input = # of bins)
	#           !!!  error value range:  [-255...0...255] = 511 possible values
	#	2)  if difference between bin's lower & upper,
	#           assign new difference value that is median between the two

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
	while(upperbound < len(range(-255, 256))):
		while(lowerbound < upperbound):
			bins[key] = median
			key = key + 1
			lowerbound = lowerbound + 1
		upperbound = upperbound + binsize
		median = lowerbound + offset
		
	#iterate through img, and replace error values with quantized values
	#for speed, search for matching bin with binary search
	#needs to called recursively	
	errorQuantized = list()
	index = 1
	for pixel in img:			# TODO::NEED TO OFFSET FOR INITIAL DATA
		errorQuantized[index] = bins[pixel]  #bins[pixel] returns value, which is new error val
											 #and is placed in new list	
    if m is None:
        return error

    raise NotImplementedError("TODO: Implement error quantization functionality")
