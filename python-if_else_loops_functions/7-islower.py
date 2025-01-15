#!/usr/bin/env python3

def islower(c):
  """
  Checks if a character is lowercase.

  Args:
    c: The character to check.

  Returns:
    True if c is lowercase, False otherwise.
  """
  if ord('a') <= ord(c) <= ord('z'):
    return True
  else:
    return False
