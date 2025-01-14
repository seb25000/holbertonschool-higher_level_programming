# Python - if/else, loops, and functions

This repository contains Python scripts and functions that focus on learning and practicing if/else statements, loops, and functions. Each task demonstrates specific programming concepts and problem-solving techniques.

## Table of Contents

1. [Positive anything is better than negative nothing](#0-positive-anything-is-better-than-negative-nothing)
2. [The last digit](#1-the-last-digit)
3. [The alphabet game](#2-the-alphabet-game)
4. [Hexadecimal printing](#4-hexadecimal-printing)
5. [00...99](#5-00-99)
6. [Two-digit combinations](#6-two-digit-combinations)
7. [islower](#7-islower)
8. [To uppercase](#8-to-uppercase)
9. [Last digit of a number](#9-last-digit-of-a-number)
10. [Addition](#10-addition)
11. [Power function](#11-power-function)
12. [FizzBuzz](#12-fizzbuzz)

## Tasks

### 0. Positive anything is better than negative nothing
**File:** `0-positive_or_negative.py`

This script assigns a random signed number to the variable `number` and prints whether the number is positive, negative, or zero.

#### Requirements:
- The output format:
  - `X is positive`
  - `X is zero`
  - `X is negative`
- Do not modify the provided `import` and `random.randint` code.

#### Example:
```bash
guillaume@ubuntu:~/$ ./0-positive_or_negative.py
-4 is negative
guillaume@ubuntu:~/$
```

---

### 1. The last digit
**File:** `1-last_digit.py`

This script prints the last digit of a random signed number along with its properties.

#### Requirements:
- The output format:
  - `Last digit of X is Y and is greater than 5`
  - `Last digit of X is Y and is 0`
  - `Last digit of X is Y and is less than 6 and not 0`

#### Example:
```bash
guillaume@ubuntu:~/$ ./1-last_digit.py
Last digit of 4205 is 5 and is less than 6 and not 0
guillaume@ubuntu:~/$
```

---

### 2. The alphabet game
**File:** `2-print_alphabet.py`

Prints the ASCII lowercase alphabet on a single line without storing characters in variables or importing modules.

#### Example:
```bash
guillaume@ubuntu:~/$ ./2-print_alphabet.py
abcdefghijklmnopqrstuvwxyzguillaume@ubuntu:~/$
```

---

### 3. Exclude q and e
**File:** `3-print_alphabt.py`

Prints the ASCII lowercase alphabet excluding the letters `q` and `e`.

#### Example:
```bash
guillaume@ubuntu:~/$ ./3-print_alphabt.py
abcdfghijklmnoprstuvwxyzguillaume@ubuntu:~/$
```

---

### 4. Hexadecimal printing
**File:** `4-print_hexa.py`

Prints numbers from 0 to 98 in both decimal and hexadecimal.

#### Example:
```bash
guillaume@ubuntu:~/$ ./4-print_hexa.py
0 = 0x0
1 = 0x1
2 = 0x2
...
98 = 0x62
guillaume@ubuntu:~/$
```

---

### 5. 00...99
**File:** `5-print_comb2.py`

Prints numbers from 0 to 99 in ascending order, formatted with two digits and separated by commas.

#### Example:
```bash
guillaume@ubuntu:~/$ ./5-print_comb2.py
00, 01, 02, ..., 99
guillaume@ubuntu:~/$
```

---

### 6. Two-digit combinations
**File:** `6-print_comb3.py`

Prints all unique combinations of two digits in ascending order.

#### Example:
```bash
guillaume@ubuntu:~/$ ./6-print_comb3.py
01, 02, 03, ..., 89
guillaume@ubuntu:~/$
```

---

### 7. islower
**File:** `7-islower.py`

Defines a function `islower(c)` that checks if a character is lowercase.

#### Example:
```python
print(islower("a")) # True
print(islower("H")) # False
```

---

### 8. To uppercase
**File:** `8-uppercase.py`

Defines a function `uppercase(str)` that prints a string in uppercase.

#### Example:
```python
uppercase("best") # BEST
uppercase("Best School 98 Battery street") # BEST SCHOOL 98 BATTERY STREET
```

---

### 9. Last digit of a number
**File:** `9-print_last_digit.py`

Defines a function `print_last_digit(number)` that prints and returns the last digit of a number.

#### Example:
```python
print_last_digit(98) # 8
print_last_digit(-1024) # 4
```

---

### 10. Addition
**File:** `10-add.py`

Defines a function `add(a, b)` that returns the sum of two integers.

#### Example:
```python
print(add(1, 2)) # 3
print(add(100, -2)) # 98
```

---

### 11. Power function
**File:** `11-pow.py`

Defines a function `pow(a, b)` that computes and returns `a` to the power of `b`.

#### Example:
```python
print(pow(2, 2)) # 4
print(pow(-4, 5)) # -1024
```

---

### 12. FizzBuzz
**File:** `12-fizzbuzz.py`

Defines a function `fizzbuzz()` that prints numbers from 1 to 100, replacing multiples of 3 with `Fizz`, multiples of 5 with `Buzz`, and multiples of both with `FizzBuzz`.

#### Example:
```python
fizzbuzz()
# Output: 1 2 Fizz 4 Buzz Fizz ...
```

---

## Repository

- **GitHub Repository:** [holbertonschool-higher_level_programming](https://github.com/your_username/holbertonschool-higher_level_programming)
- **Directory:** `python-if_else_loops_functions`

