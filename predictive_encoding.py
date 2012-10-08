
def predict_encoding():
    """
    (Task 3): Given ???, perform one of eight predictive encoding schemes on the quantized data:

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

    raise NotImplementedError("TODO: Implement predictive encoding functionality")