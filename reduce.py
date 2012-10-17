from __future__ import division

from math import ceil

def reduce(color_channels, S=(None, None, None)): # Use default values of None until implemented
    """
    (Task 1): Given three channels c1, c2, c3 of an image, and three numbers s1, s2, s3,
    reduce the resolution of the channels of the image by 1/s1, 1/s2, 1/s3, respectively.
    """
    c1, c2, c3 = color_channels

    if any(s <= 0 for s in S):
        raise ValueError("Cannot reduce resolution by a negative or 0 value.")

    if not any(S):
        return c1, c2, c3

    s1, s2, s3 = S

    is1, is2, is3 = (1/s for s in S) # inverted s

    # Get whole parts of the number of pixels per new pixel
    is_width_pixels = (int(ceil(is_ * width)) for is_ in (is1, is2, is3))
    is_height_pixels = (int(ceil(is_ * height)) for is_ in (is1, is2, is3))

    raise NotImplementedError("TODO: Implement resolution reduction functionality")