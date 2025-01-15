#!/usr/bin/env python3

def pow(a, b):
    """Computes a to the power of b.

    Args:
        a: The base number.
        b: The exponent.

    Returns:
        The value of a^b.
    """
    if b == 0:
        return 1
    if b < 0:
       return 1 / power_positive(a, -b)
    return power_positive(a,b)
def power_positive(a,b):
    result = 1
    for _ in range(b):
      result *= a
    return result

if __name__ == "__main__":
    pow_func = pow
    print(pow_func(2, 2))
    print(pow_func(98, 2))
    print(pow_func(98, 0))
    print(pow_func(100, -2))
    print(pow_func(-4, 5))
