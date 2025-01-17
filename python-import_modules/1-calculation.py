#!/usr/bin/python3

import calculator_1
if __name__ == "__main__":


    a = 10
    b = 5

    add_result = calculator_1.add(a, b)
    sub_result = calculator_1.sub(a, b)
    mul_result = calculator_1.mul(a, b)
    div_result = calculator_1.div(a, b)


    print("a + b = {}".format(add_result))
    print("a - b = {}".format(sub_result))
    print("a * b = {}".format(mul_result))
    print("a / b = {}".format(div_result))
