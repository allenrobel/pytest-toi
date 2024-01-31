def square(x):
    if not isinstance(x, (int, float)):
        raise TypeError("x must be numeric")
    return x * x
