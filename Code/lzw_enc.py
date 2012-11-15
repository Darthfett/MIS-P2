from byte_packer import int_seq_to_bin_seq

def lzw_encode(seq):
    seq = list(seq) # make a copy
    seq.reverse() # For efficiency, we will reverse the list and get data from the end

    output = []

    dictionary = {str(s) : s for s in range(256)}
    i = 256

    try:
        s = seq.pop()
    except IndexError:
        return int_seq_to_bin_seq(output, 255)

    # dictionary = [] # TODO: Set a default set of values for the dictionary
    while True:
        try:
            c = seq.pop()
        except IndexError:
            break
        if (s + c) in dictionary:
            s = s + c
        else:
            output.append(dictionary[s])
            dictionary[s + c] = i
            i += 1
            s = c

    if s in dictionary:
        output.append(dictionary[s])
    else:
        output.append(i)
    return int_seq_to_bin_seq(output, len(dictionary))

def lzw_decode(seq):

    seq = list(seq)
    seq.reverse()

    output = []

    dictionary = {s : str(s) for s in range(256)}
    i = 256

    try:
        s = (dictionary[seq.pop()], )
    except IndexError:
        return output

    output.append(s[0])

    while True:
        try:
            k = seq.pop()
        except IndexError:
            break
        if k in dictionary:
            entry = dictionary[k]
        elif k == i:
            entry = s + (s[0], )

        if isinstance(entry, str):
            output.append(entry)
            dictionary[i] = s + (entry, )
            i += 1
        else:
            output.extend(entry)
            dictionary[i] = s + (entry[0], )
            i += 1
        if isinstance(entry, str):
            s = (entry, )
        else:
            s = entry
    return output

# a = ['255', '254', '255', '255', '255', '255', '255', '255', '255', '255', '255', '255']
# print(a)
# b = lzw_encode(a)
# print(b)
# c = lzw_decode(b)
# print(c)

# import Image as pil
# from test import *
# img = pil.open('test.png')
# pixels = img.getdata()
# rch, gch, bch = zip(*pixels)
# rch, gch, bch = list(map(str, rch)), list(map(str, gch)), list(map(str, bch))
# r_enc = lzw_encode(rch)
# r_dec = lzw_decode(r_enc)
# count = 0
# for i, val in enumerate(r_dec):
    # if val != rch[i]:
        # print("Index {i}, original: {o}, new: {n}".format(i=i, o=rch[i], n=val))
#         count+=1
        # if count > 30:
            # break
# print(r_dec == rch)