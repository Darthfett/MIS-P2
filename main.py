
from __future__ import print_function
from __future__ import division

# 3rd party modules
import Image as pil

# builtin modules
import os
import sys
import itertools as it

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
reduce_S = (None, None, None, None, None, None) # holds s1x, s1y, s2x, s2y, s3x, s3y values

def RGB_to_YCbCr(r, g, b):
    return (r, g, b) # For debugging
    r /= 255
    g /= 255
    b /= 255
    y =  int((0.299 * r +  0.587 * g +  0.144 * b) * 255)
    cb = int((-0.168736 * r + -0.331264 * g + 0.5 * b + 0.5) * 255)
    cr = int((0.5 * r + -0.418688 * g + -0.081312 * b + 0.5) * 255)
    return (y, cb, cr)

def get_channels(image):
    """Get a list of tuples containing the Ys, Cbs, and Crs of the image."""
    YCbCr = [RGB_to_YCbCr(*pix) for pix in image.getdata()]
    Y, Cb, Cr = zip(*YCbCr) # matrix transform
    return Y, Cb, Cr

def get_image():
    image = None
    while image is None:
        image_path = raw_input("Select an image: ")
        try:
            image = pil.open(image_path)
        except Exception:
            pass
    return image

def get_reduce_S():
    print("Enter in reduction parameters (6 integers: a 1 results in no reduction)")
    s_str = ['red width', 'red height', 'green width', 'green height', 'blue width', 'blue height']

    s_val = []
    for str_ in s_str:
        s = None
        while s is None:
            s_input = raw_input(str_ + ': ')
            if not s_input:
                s = 1
                break

            try:
                int(s_input)
            except ValueError:
                print("Invalid input")
                continue

            if int(s_input) != 0:
                s = int(s_input)
            else:
                print("Invalid input")
        s_val.append(s)

    # default values to reduce_S values if the user enters ''
    S = tuple((s if s is not None else reduce_S[i]) for i, s in enumerate(s_val))
    return tuple(map(tuple, (S[0:2], S[2:4], S[4:6])))

def get_quantization_bins():
    prompt = "Number of bins to quantize {} channel: "
    bin_str = ['red', 'blue', 'green']

    bin_vals = []
    for str_ in bin_str:
        bin_val = None
        while bin_val is None:
            bin_input = raw_input(prompt.format(str_))
            if not bin_input:
                break
            try:
                int(bin_input)
            except ValueError:
                print("Invalid input")
                continue

            if int(bin_input) > 0:
                bin_val = int(bin_input)
            else:
                print("Invalid input")
        bin_vals.append(bin_val)

    return bin_vals


# Command functions

def display(image, *args):
    """
    Attempts to display the image

    NOTE: PIL's image.show can have problems on windows, as some viewers do not work properly.
    See: http://stackoverflow.com/questions/8932976/python-imaging-library-show-on-windows
    """
    image.show()

def encoding_delegate(image, channels, *args):
    """
    Will need to get an array that contains:
        1. a value informing what encoding is needed.
        2. an array of values to encode. Assuming RGB values.

    Will return an array with encoded values.
    """

    scheme = None
    while scheme is None:
        scheme_input = raw_input("Choose encoding scheme (2: Shannon Fanno, 3: LZW): ")

        if not scheme_input:
            break

        try:
            scheme_int = int(scheme_input)
        except ValueError:
            print("Invalid input")
            continue

        if scheme_int not in (1, 2, 3):
            print("Invalid input")
            continue

        scheme = scheme_int

    # t5_output = [[str(s) for s in ch] for ch in channels]

    t5_output = channels
    t5_output = [encoding.encode(channel, scheme) for channel in t5_output]
    t5_output = [encoding.decode(encoding, scheme) for encoding in t5_output]

    # t5_output = [[int(s) for s in ch] for ch in t5_output]

    return t5_output

def error_delegate(image, error, *args):
    bins = None
    while bins is None:
        bin_input = raw_input("Number of bins to quantize error: ")

        if not bin_input:
            break

        try:
            bin_int = int(bin_input)
        except ValueError:
            print("Invalid input")
            continue

        if int(bin_input) < 1:
            print("Invalid input")
            continue
        else:
            bins = int(bin_input)

    t4_output = eq.error_quantization(image, error, bins)
    return t4_output

def help(image, *args):
    print(HELP)

def output_delegate(image, *args):
    with open('test.YBR', 'wb') as out:
        out.write(str(args[0]))
    pass

def predict_delegate(image, t2_output, widths, heights, *args):
    predict_type = -1
    while (predict_type<1 or predict_type>8):
        predict_type = raw_input("Type of prediction (integer 1-8): ")
        if not predict_type:
            # Default choice is to do no predictive coding (original values)
            predict_type = 1
            break
        try:
            predict_type = int(predict_type)
        except ValueError:
            predict_type = -1
        if (predict_type < 1 or predict_type > 8):
            print("Invalid input")
    predicted_channels = pe.predict_encoding(t2_output, widths, heights, predict_type)
    return predicted_channels


    # Need to validate predict_type as a valid integer (use a while loop to continue asking user?  See get_quantization_bins for example

    # Call pe.predict_encoding with values

def quantization_delegate(image, channels, *args):
    bins = get_quantization_bins()

    quantized_channels = quantization.quantize(channels, bins)

    return quantized_channels

def reduce_delegate(image, *args):
    channels = get_channels(Image)
    new_channels = reduce.reduce(channels, image.size[0], reduce_S)
    heights = [len(ch) for ch in new_channels]
    widths = [len(channel[0]) for channel in new_channels] # width of new image

    flat_channels = [list(it.chain.from_iterable(ch)) for ch in new_channels]
    flat_channels = [[int(px) for px in ch] for ch in flat_channels]

    print("Image reduced from {w}x{h} to R:{rw}x{rh}, G:{gw}x{gh}, B:{bw}x{bh}".format(
            w=image.size[0], h=image.size[1], rw=widths[0], rh = heights[0],
            gw=widths[1], gh=heights[1], bw=widths[2], bh=heights[2]))

    return flat_channels, widths, heights

    # temp code to save 3 channels into an image, assuming all channels are the same length.
    # pixels = zip(*flat_channels) # A list of tuples containing (R, G, B)
    # pixels = [(int(p1), int(p2), int(p3)) for p1, p2, p3 in pixels] # Integerize the tuples
    # image = pil.new('RGB', (width, height)) # Create a new destination image for the pixels
    # image.putdata(pixels) # copy in the pixels
    # image.save("test2.png", 'PNG') # save the image to a test file
    # print("saved")

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
    global Image, reduce_S

    Image = get_image()

    print("Task 1")
    print("================")
    # Task 1: reduce data for each channel
    reduce_S = get_reduce_S()
    reduced_channels, new_widths, new_heights = reduce_delegate(Image)
    print("================")

    print("Task 2")
    print("================")
    # Task 2: quantization of the channels into bins
    t2_output = quantization_delegate(Image, reduced_channels)
    print("================")

    print("Task 3")
    print("================")
    # TODO: What is the output of Task 2 and what does Task 3 require as input?
    # Task 3: Predictive coding
    t3_output = predict_delegate(Image, t2_output, new_widths, new_heights)
    print("================")

    print("Task 4")
    print("================")
    # TODO: What is the output of Task 3 and what does Task 4 require as input?
    # Task 4: Error quantization
    t4_output = error_delegate(Image, t3_output)
    print("================")

    print("Task 5")
    print("================")
    # TODO: What is the output of Task 4 and what does Task 5 require as input?
    # Task 5: Encoding scheme
    t5_output = encoding_delegate(Image, t4_output)
    print("================")

    print("Task 6")
    print("================")
    # Task 6: Output
    output_delegate(Image, t5_output)
    print("================")


def main_old(args):
    global Image, reduce_S
    Image = get_image()
    reduce_S = get_reduce_S()
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
        CMD_DICT[cmd](Image, *args)

    # display(Image)


if __name__ == '__main__':
    main(sys.argv[1:]) # Skip first argument ("main.py").