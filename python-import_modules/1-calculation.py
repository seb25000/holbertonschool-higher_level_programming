#!/usr/bin/python3

import calculator_1

if __name__ == "__main__":
    a = 10
    b = 5

    # Use the imported functions with 'a' and 'b'
    result_add = calculator_1.add(a, b)
    result_sub = calculator_1.sub(a, b)
    result_mul = calculator_1.mul(a, b)
    result_div = calculator_1.div(a, b)

    # Display results (print statements are limited to 4)
    print(f"{a} + {b} = {result_add}")
    print(f"{a} - {b} = {result_sub}")
    print(f"{a} * {b} = {result_mul}")
    print(f"{a} / {b} = {result_div}")
