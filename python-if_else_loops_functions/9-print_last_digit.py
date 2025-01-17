#!/usr/bin/python3

def print_last_digit(number):
    """Prints the last digit of a number and returns it."""
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit

if __name__ == '__main__':
    print_last_digit = __import__('9-print_last_digit').print_last_digit

    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
    