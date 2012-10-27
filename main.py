
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
encoding: choose the encoding scheme
error: choose the error quantization parameters
help: display this message
predict: choose a predictive encoding algorithm
quantization: choose the number of bins to quantize
reduce: choose the resolution reduction parameters
save: save the image to the disk
select: select a new image
"""

Image = None

def get_channels(image):
    """Get a list of tuples containing the reds, greens, and blues of the image."""
    RGB = image.getdata()
    r, g, b = zip(*RGB) # matrix transform
    return r, g, b

def get_image():
    image = None
    while image is None:
        image_path = raw_input("Select an image: ")
        try:
            image = pil.open(image_path)
        except Exception:
            pass
    return image

# Command functions

def display(image, *args):
    """
    Attempts to display the image

    NOTE: PIL's image.show can have problems on windows, as some viewers do not work properly.
    See: http://stackoverflow.com/questions/8932976/python-imaging-library-show-on-windows
    """
    image.show()

def encoding_delegate(image, *args):
    pass

def error_delegate(image, *args):
    pass

def help(image, *args):
    print(HELP)

def predict_delegate(image, *args):
    pass

def quantization_delegate(image, *args):
    pass

def reduce_delegate(image, *args):
    pass

def save(image, *args):
    filename = raw_input('Filename: ')
    try:
        image.save(filename, 'PNG')
    except Exception:
        return None
    return image

def select(image, *args):
    Image = get_image()

CMD_DICT = {
    'display': display,
    'encoding': encoding_delegate,
    'error': error_delegate,
    'help': help,
    'predict': predict_delegate,
    'quantization': quantization_delegate,
    'reduce': reduce_delegate,
    'save': save,
    'select': select,
}

def main(args):
    Image = get_image()
    channels = get_channels(Image)
    while True:
        # Accept a command with args from the user (and split into a list)
        command = raw_input('Enter a command (or "help"): ').strip().split(' ')

        cmd = command[0].lower() # command is case-insensitive
        args = command[1:]

        # validate cmd to be a valid command
        if cmd not in CMD_DICT:
            if not cmd:
                # no command entered
                cmd = 'help'
            elif any(command.startswith(cmd) for command in CMD_DICT):
                # command is not an exact match, try a partial match
                cmd = next(command for command in CMD_DICT if command.startswith(cmd))

        if cmd not in CMD_DICT:
            # command is a quit, exit, or invalid command.
            if cmd.startswith(('q', 'e')):
                break
            print('Invalid command "{cmd}".  Valid commands: {cmds}'.format(cmd=cmd, cmds=', '.join(sorted(CMD_DICT.keys()))))
            continue
        # At this point, cmd is a valid command.
        CMD_DICT[cmd](Image, channels[:], *args)

    # display(Image)


if __name__ == '__main__':
    main(sys.argv[1:]) # Skip first argument ("main.py").