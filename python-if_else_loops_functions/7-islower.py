#!/usr/bin/env python3

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

#!/usr/bin/env python3
islower = __import__('7-islower').islower

print("a is {}".format("lower" if islower("a") else "upper"))
print("H is {}".format("lower" if islower("H") else "upper"))
print("A is {}".format("lower" if islower("A") else "upper"))
print("3 is {}".format("lower" if islower("3") else "upper"))
print("g is {}".format("lower" if islower("g") else "upper"))
