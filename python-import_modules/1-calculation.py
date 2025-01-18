#!/usr/bin/python3

import calculator_1

# Définition des variables
a = 10
b = 5

# Effectuer les calculs et stocker les résultats
addition_result = calculator_1.add(a, b)
subtraction_result = calculator_1.sub(a, b)
multiplication_result = calculator_1.mul(a, b)
division_result = calculator_1.div(a, b)

# Affichage des résultats avec seulement 4 appels à print
print(f"{a} + {b} = {addition_result}")
print(f"{a} - {b} = {subtraction_result}")
print(f"{a} * {b} = {multiplication_result}")
print(f"{a} / {b} = {division_result}")
