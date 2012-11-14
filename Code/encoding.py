import collections
from shanfan_enc import shanfan_encode
from shanfan_enc import shanfan_decode
from lzw_enc import lzw_encode
from lzw_enc import lzw_decode
from byte_packer import int_seq_to_bin_seq

ENCODING_SCHEME_NONE = 1
ENCODING_SCHEME_VARLEN = 2
ENCODING_SCHEME_DICT = 3

DEBUG_VERBOSE = True

def list2string(alist):
    output = ''
    output += ''.join(map(str, seq))
    return alist

#(Task 5): Given ???, perform the following encoding schemes:
#    - Encoding Option 1: No encoding
#    - Encoding Option 2: Variable-length encoding with Shanno-Fano coding
#    - Encoding Option 3: Dictionary encoding with LZW coding (for a given dictionary bit length)

def encode( chan, opcode):
    if( opcode == ENCODING_SCHEME_VARLEN):
        return shanfan_encode(chan)[0]
    if( opcode == ENCODING_SCHEME_DICT):
        chan = [str(s) for s in chan]
        return lzw_encode(chan)

    else:
        return int_seq_to_bin_seq(chan, 255)

def decode( chan, opcode):
    if( opcode == ENCODING_SCHEME_VARLEN):
        return shanfan_decode(chan)
    if( opcode == ENCODING_SCHEME_DICT):
        result = lzw_decode(chan)
        result = [int(s) for s in result]
        return result
    else:
        return chan
