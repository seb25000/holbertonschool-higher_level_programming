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
    if b > 0:
      result = 1
      for _ in range(b):
        result *= a
      return result
    else:
      result = 1
      for _ in range(abs(b)):
        result /= a
      return result
