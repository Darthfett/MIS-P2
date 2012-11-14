from itertools import izip_longest
from math import ceil, log

def grouper(n, iterable, fillvalue=None):
    "Collect data into fixed-length chunks or blocks"
    # grouper(3, 'ABCDEFG', 'x') --> ABC DEF Gxx
    args = [iter(iterable)] * n
    return izip_longest(fillvalue=fillvalue, *args)

def num_bits(max_size):
    """
    Given an unsigned number of maximum value max_size, get the number of bits needed to represent that number.
    """
    if (max_size <= 0):
        raise ValueError("Find number of bits needed to represent an integer with max value of 0?")
    return int(ceil(log(max_size + 1, 2)))

def int_to_bin(i, bitlen):
    seq = bin(i)[2:]
    if len(seq) % bitlen:
        seq = '0' * (bitlen - (len(seq) % bitlen)) + seq

    return seq

def binary_seq_to_bytearray(seq):
    if len(seq) % 8:
        seq += '0' * (8 - (len(seq) % 8))
    return seq

def int_seq_to_bin_seq(seq, int_max_size):
    seq = list(seq)
    bits_per_int = num_bits(int_max_size)

    # Get the last bits_per_int of each value
    bit_list = [int_to_bin(v, bits_per_int) for v in seq]

    # Get a sequence of 0s and ones
    bin_seq = binary_seq_to_bytearray(''.join(bit_list))
    return bin_seq

def int_seq_to_bytearray(seq, int_max_size):
    # get binary sequence
    bin_seq = int_seq_to_bin_seq(seq, int_max_size)

    # pack the bits into bytes
    int_list = [int(''.join(x), 2) for x in grouper(8, bin_seq, '0')]

    return int_list
    return bytearray(int_list)

def bin_seq_to_bytearray(bin_seq):
    # pack the bits into bytes
    int_list = [int(''.join(x), 2) for x in grouper(8, bin_seq, '0')]

    return int_list
    return bytearray(int_list)