#!/usr/bin/python3

def add(a, b):
    """Adds two integers.

    Args:
        a: The first integer.
        b: The second integer.

    Returns:
        The sum of a and b.
    """
    return a + b

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    result = add(a, b)
    print("{:d} + {:d} = {:d}".format(a, b, result))
