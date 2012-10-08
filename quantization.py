
def quantize(c1, c2, c3, n1=None, n2=None, n3=None): # Default values of None to indicate no quantization.
    """
    (Task 2): Given three channels c1, c2, c3 of an image, and three numbers n1, n2, n3,
    uniformly quantize the channels into n1, n2, n3 bins respectively.
    """
    if not any({n1, n2, n3}):
        return c1, c2, c3
    
    raise NotImplementedError("TODO: Implement uniform quantization functionality")