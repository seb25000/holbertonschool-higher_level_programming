#!/usr/bin/env python3

def uppercase(str):
    uppercase_str = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        uppercase_str += uppercase_char
    print("{}".format(uppercase_str))


if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
