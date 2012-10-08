
def quantize(color_channels, N=((None,)*3)): # Default values of None to indicate no quantization.
    """
    (Task 2): Given three channels c1, c2, c3 of an image, and three numbers n1, n2, n3,
    uniformly quantize the channels into n1, n2, n3 bins respectively.
    """
    c1, c2, c3 = color_channels
    n1, n2, n3 = N

    if not any({n1, n2, n3}):
        return c1, c2, c3

    raise NotImplementedError("TODO: Implement uniform quantization functionality")