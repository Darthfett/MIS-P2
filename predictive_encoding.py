
def predict_encoding(original_colors, quantized_colors):
    """
    (Task 3): Given three channels original_colors=[c1, c2, c3] and three channels quantized_colors=[q1, q2, q3] of an image,
    perform one of eight predictive encoding schemes on the quantized data (this interface is subject to change).
    
    – PC Option 1: No PC (use original values).
    – PC Option 2: Predictive encoding with the predictor A.
    – PC Option 3: Predictive encoding with the predictor B.
    – PC Option 4: Predictive encoding with the predictor C.
    – PC Option 5: Predictive encoding with the predictor (A+B+C) / 3.
    – PC Option 6: Predictive encoding with the predictor A + (B - C) = B + (A - C).
    – PC Option 7: Predictive encoding with the predictor (A+B) / 2.
    – PC Option 8: Predictive encoding with the predictor:
        * if B - C > 0 and A - C > 0 then C + sqrt((B - C)^2 + (A - C)^2),
        * else if B - C < 0 and A - C < 0 then C - sqrt((B - C)^2 + (A - C)^2,
        * else (A+B) / 2.
    
    """
    c1, c2, c3 = original_colors
    q1, q2, q3 = quantized_colors
    
    raise NotImplementedError("TODO: Implement predictive encoding functionality")