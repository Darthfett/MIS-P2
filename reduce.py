
def reduce(c1, c2, c3, s1=1, s2=1, s3=1): # Use default values of 1 until implemented
    """
    (Task 1): Given three channels c1, c2, c3 of an image, and three numbers s1, s2, s3,
    reduce the resolution of the channels of the image by 1/s1, 1/s2, 1/s3, respectively.
    """
    if s1 == s2 == s3 == 1:
        return c1, c2, c3
    
    raise NotImplementedError("TODO: Implement resolution reduction functionality")