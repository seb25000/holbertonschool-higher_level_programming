#!/usr/bin/python3

def add(a, b):
  """Adds two integers and returns the result.

  Args:
    a: The first integer.
    b: The second integer.

  Returns:
    The sum of a and b.
  """
  return a + b

if __name__ == "__main__":
    add = __import__('10-add').add
    print(add(1, 2))
    print(add(98, 0))
    print(add(100, -2))
