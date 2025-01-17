# Python - Import & Modules

# Description

This project explores the concepts of importing functions and modules in Python, using command line arguments, and adhering to style guidelines. 

# Learning Objectives

By the end of this project, you will be able to:

*   Explain why Python programming is awesome.
*   Import functions from another file.
*   Use imported functions.
*   Create a module.
*   Use the built-in function `dir()`.
*   Prevent code in your script from being executed when imported.
*   Use command line arguments with your Python programs.

## Requirements

### General
*   **Allowed editors:** vi, vim, emacs
*   **Operating System:** Ubuntu 22.04 LTS using Python3 (version 3.10.\*)
*   **File format:** All files must end with a new line.
*   **Shebang:** The first line of all your files should be exactly `#!/usr/bin/python3`.
*   **README.md:** A `README.md` file at the root of the project is mandatory.
*   **Code style:** Your code should use the `pycodestyle` (version 2.7.\*).
*   **File Permissions:** All your files must be executable.
*   **File length:** File lengths will be checked with `wc`.

## Tasks

### 0. Import a simple function from a simple file
*   **File**: `0-add.py`
*   Write a program that imports the function `def add(a, b):` from the file `add_0.py` and prints the result of the addition `1 + 2 = 3`.
*   Use string formatting to display integers.
*   Assign the value `1` to a variable `a` and `2` to `b`.
*   `a` and `b` must be defined on separate lines.
*   Use the `add` function with `a` and `b` as arguments.
*   The program should print: `<a value> + <b value> = <add(a, b) value>` followed by a new line.
*   Only use the word `add_0` once.
*   Do not use `*` for importing or `__import__`.
*   Your code should not be executed when imported (by using `__name__ == "__main__"`).
    
    ```bash
    guillaume@ubuntu:~/python-import_modules$ cat add_0.py
    #!/usr/bin/python3
    def add(a, b):
        """My addition function

        Args:
            a: first integer
            b: second integer

        Returns:
            The return value. a + b
        """
        return (a + b)
    
    guillaume@ubuntu:~/python-import_modules$ ./0-add.py
    1 + 2 = 3
    guillaume@ubuntu:~/python-import_modules$ cat 0-import_add.py
    __import__("0-add")
    guillaume@ubuntu:~/python-import_modules$ python3 0-import_add.py 
    guillaume@ubuntu:~/python-import_modules$
    ```

### 1. My first toolbox!
*   **File:** `1-calculation.py`
*   Write a program that imports functions from the file `calculator_1.py`, performs math operations, and prints the results.
*   Do not use the `print` function more than 4 times.
*   Define `a = 10` and `b = 5` on separate lines and only use them in function calls.
*   Your program should call each imported function.
*   Use `calculator_1` only once.
*   Do not use `*` for importing or `__import__`.
*   Your code should not be executed when imported.
    
    ```bash
    guillaume@ubuntu:~/python-import_modules$ cat calculator_1.py
    #!/usr/bin/python3
    def add(a, b):
        """My addition function
    
        Args:
            a: first integer
            b: second integer
    
        Returns:
            The return value. a + b
        """
        return (a + b)
    
    
    def sub(a, b):
        """My subtraction function
    
        Args:
            a: first integer
            b: second integer
    
        Returns:
            The return value. a - b
        """
        return (a - b)
    
    
    def mul(a, b):
        """My multiplication function
    
        Args:
            a: first integer
            b: second integer
    
        Returns:
            The return value. a * b
        """
        return (a * b)
    
    
    def div(a, b):
        """My division function
    
        Args:
            a: first integer
            b: second integer
    
        Returns:
            The return value. a / b
        """
        return int(a / b)
    
    guillaume@ubuntu:~/python-import_modules$ ./1-calculation.py
    10 + 5 = 15
    10 - 5 = 5
    10 * 5 = 50
    10 / 5 = 2
    guillaume@ubuntu:~/python-import_modules$
    ```

### 2. How to make a script dynamic!
*   **File:** `2-args.py`
*   Write a program that prints the number and list of command-line arguments.
*   The output format should be as follows:
    *   `Number of argument(s) followed by argument (if number is one) or arguments (otherwise), followed by` `: (or . if no arguments were passed) followed by` `a new line`
    *   (If at least one argument) one line per argument with the position (starting at 1) followed by `:`, followed by the argument value, and a new line
*   Your code should not be executed when imported.

    ```bash
    guillaume@ubuntu:~/python-import_modules$ ./2-args.py 
    0 arguments.
    guillaume@ubuntu:~/python-import_modules$ ./2-args.py Hello
    1 argument:
    1: Hello
    guillaume@ubuntu:~/python-import_modules$ ./2-args.py Hello Welcome To The Best School
    6 arguments:
    1: Hello
    2: Welcome
    3: To
    4: The
    5: Best
    6: School
    guillaume@ubuntu:~/python-import_modules$ 
    ```

### 3. Infinite addition
*   **File:** `3-infinite_add.py`
*   Write a program that prints the sum of all command-line arguments.
*   Cast arguments to integers using `int()`.
*   Your code should not be executed when imported.

    ```bash
    guillaume@ubuntu:~/python-import_modules$ ./3-infinite_add.py
    0
    guillaume@ubuntu:~/python-import_modules$ ./3-infinite_add.py 79 10
    89
    guillaume@ubuntu:~/python-import_modules$ ./3-infinite_add.py 79 10 -40 -300 89 
    -162
    guillaume@ubuntu:~/python-import_modules$ 
    ```

### 4. Who are you?
*   **File:** `4-hidden_discovery.py`
*   Write a program that prints all the names defined in the compiled module `hidden_4.pyc`. Download this file locally in your sandbox using `curl`.
*   The file `4-hidden_discovery.py` should be located in the `/tmp/` folder.
*   Print one name per line, in alphabetical order.
*   Only print names that do not start with `__`.
*   Your code should not be executed when imported.
    
    ```bash
    guillaume@ubuntu:/tmp$ curl -Lso "hidden_4.pyc" "https://github.com/hs-hq/0x02.py/raw/main/hidden_4.pyc"
    guillaume@ubuntu:/tmp$ ./4-hidden_discovery.py | sort
    my_secret_santa
    print_hidden
    print_school
    guillaume@ubuntu:/tmp$
    ```

### 5. Everything can be imported
*   **File:** `5-variable_load.py`
*   Write a program that imports the variable `a` from the file `variable_load_5.py` and prints its value.
*   Do not use `*` for importing or `__import__`.
*   Your code should not be executed when imported.
    
    ```bash
    guillaume@ubuntu:~/python-import_modules$ cat variable_load_5.py
    #!/usr/bin/python3
    a = 98
    """Simple variable
    """
    
    guillaume@ubuntu:~/python-import_modules$ ./5-variable_load.py
    98
    guillaume@ubuntu:~/python-import_modules$
    ```
