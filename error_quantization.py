
def error_quantization(original_colors, quanitzed_colors, error, m=None):
    """
    (Task 4): Given three channels original_colors =[c1, c2, c3],
                                   quantized_colors=[q1, q2, q3],
                                   error, and m,
    perform uniform OR non-uniform quantization of the error into m bins.
    """
    c1, c2, c3 = original_colors
    q1, q2, q3 = quantized_colors
    
    if m is None:
        return error
    
    raise NotImplementedError("TODO: Implement predictive encoding functionality")