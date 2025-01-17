#!/usr/bin/python3


def islower(c):

    """Checks if a character is lowercase.

    Args:
        c: The character to check.

    Returns:
        True if c is lowercase, False otherwise.
    """
    ascii_val = ord(c)
    if 97 <= ascii_val <= 122:
        return True
    else:
        return False
