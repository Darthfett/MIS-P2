from __future__ import division

from math import ceil, floor

def get_square(channel, width, left, sq_width, top, sq_height):
    rows = []
    for i in range(sq_height):
        rows.extend(channel[((top + i) * width) + left : ((top + i) * width) + (left + sq_width)])
    return rows

def reduce_channel(channel, width, sx, sy):
    height = len(channel) // width
    new_width = int(round(width / sx))
    new_height = int(round(height / sy))

    # There are now scale x scale pixels per new pixel

    new_chan = []
    new_row = []
    for row in range(new_height):
        for col in range(new_width):
            left = sx * col
            top = sy * row
            square = get_square(channel, width, left, sx, top, sy)
            if len(new_row) >= new_width:
                new_chan.append(tuple(new_row))
                new_row = []
            new_row.append(sum(square) / len(square))
    new_chan.append(tuple(new_row))
    return new_chan



def reduce(color_channels, width, S=((None, None), (None, None), (None, None))): # Use default values of None until implemented
    """
    (Task 1): Given three channels c1, c2, c3 of an image, and three numbers s1, s2, s3,
    reduce the resolution of the channels of the image by 1/s1, 1/s2, 1/s3, respectively.
    """
    c1, c2, c3 = color_channels

    if not all(s for SI in S for s in SI):
        raise ValueError("Cannot reduce resolution by a None value.")
        # return c1, c2, c3

    if any(s <= 0 for SI in S for s in SI):
        raise ValueError("Cannot reduce resolution by a negative or 0 value.")

    s1, s2, s3 = S

    # reduced channels
    c1_r = reduce_channel(c1, width, *s1)
    c2_r = reduce_channel(c2, width, *s2)
    c3_r = reduce_channel(c3, width, *s3)

    return c1_r, c2_r, c3_r