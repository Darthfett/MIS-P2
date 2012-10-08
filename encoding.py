
ENCODING_SCHEME_NONE = 1
ENCODING_SCHEME_VARLEN = 2
ENCODING_SCHEME_DICT = 3

def encoding(original_colors, quanitzed_colors, error, encoding):
    """
    (Task 5): Given three channels original_colors =[c1, c2, c3],
                                   quantized_colors=[q1, q2, q3],
                                   error,
    Perform the following encoding schemes:
        – Encoding Option 1: No encoding
        – Encoding Option 2: Variable-length encoding with Shannon-Fano coding
        – Encoding Option 3: Dictionary encoding with LZW coding (for a given dictionary bit length)
    """
    
    c1, c2, c3 = original_colors
    q1, q2, q3 = quantized_colors
    
    raise NotImplementedError("TODO: Implement predictive encoding functionality")