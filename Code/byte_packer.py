from itertools import islice

def take(n, iterable): # Taken from itertools Recipes library
    """Return first n items of the iterable as a list"""
    return list(islice(iterable, n))

def num_bits(max_size):
    """
    Given an unsigned number of maximum value max_size, get the number of bits needed to represent that number.
    """
    if (max_size <= 0):
        raise ValueError("Find number of bits needed to represent an integer with max value of 0?")
    return 2 ** (max_size - 1)

def binary_seq_to_bytearray(seq):
    if len(seq) % 8:
        seq += '0' * (8 - (len(seq) % 8))
    return seq

def int_seq_to_bin_seq(seq, int_max_size):
    bits_per_int = num_bits(int_max_size)

    # Get the last bits_per_int of each value
    bit_list = [bin(v)[-bits_per_int:] for v in seq]

    # Get a sequence of 0s and ones
    bin_seq = binary_seq_to_bytearray(''.join(bit_list))
    return bin_seq

def int_seq_to_bytearray(seq, int_max_size):
    # get binary sequence
    bin_seq = int_seq_to_bin_seq(seq, int_max_size)

    # pack the bits into bytes
    int_list = [int(x) for x in take(8, bin_seq)]


    return bytearray(int_list)

def bin_seq_to_bytearray(bin_seq):
    # pack the bits into bytes
    int_list = [int(x) for x in take(8, bin_seq)]


    return bytearray(int_list)