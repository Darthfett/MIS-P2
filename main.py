
from __future__ import print_function
from __future__ import division

# 3rd party modules
import Image as pil

# builtin modules
import os
import sys

# project modules
import reduce
import quantization
import predictive_encoding as pe
import error_quantization as eq
import encoding

HELP = """

display: display the image
encoding: choose the encoding scheme
error: choose the error quantization parameters
help: display this message
predict: choose a predictive encoding algorithm
quantization: choose the number of bins to quantize
reduce: choose the resolution reduction parameters
save: save the image to the disk
select: select a new image

""".strip()

def display(image, *args):
    image.show()

def help(image, *args):
    print(HELP)

def save(image, *args):
    filename = raw_input('Filename: ')
    try:
        image.save(filename, 'PNG')
    except Exception:
        return None
    return image



def main(args):
    pass

if __name__ == '__main__':
    main(sys.argv[1:]) # Skip first argument ("main.py").