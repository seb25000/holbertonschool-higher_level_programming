# Enhancing Code Quality and Efficiency with ChatGPT

Welcome to a specialized module of our IT curriculum where we explore innovative ways to integrate artificial intelligence into everyday coding practices.

This project focuses on two pivotal aspects of software development: debugging and automation. By engaging with these tasks, you’ll learn how to harness the capabilities of ChatGPT to not only identify and resolve errors more efficiently but also to automate repetitive coding tasks, thereby increasing your productivity and improving the quality of your code.

## Objectives

*   **Debugging:** Understand the practical use of AI in identifying and solving coding errors. You will use ChatGPT to diagnose and correct bugs in provided code samples across multiple programming languages. This will enhance your problem-solving skills and understanding of common programming pitfalls in a diverse set of coding environments.
*   **Automation:** Learn how to automate mundane and repetitive coding tasks with the assistance of ChatGPT. This involves generating boilerplate code, documentation, and even basic unit tests, freeing up time to focus on more complex and creative aspects of software development.

## Outcomes

*   **Enhanced Debugging Skills:** Gain confidence in troubleshooting and refining code, with an ability to articulate problems clearly and implement AI-driven solutions effectively.
*   **Automation Proficiency:** Develop skills to leverage AI for automating coding tasks, leading to more structured and error-free code.

Through this project, you will engage in hands-on activities that reflect real-world scenarios, pushing the boundaries of traditional coding methods with AI integration. This approach not only prepares you for future technological advancements but also equips you with skills that are increasingly in demand in the tech industry. Get ready to transform the way you code by making it smarter, faster, and more efficient!

**Remember to test, verify, and critically evaluate the information provided by ChatGPT. Don’t hesitate to question or double-check the responses to ensure their accuracy and relevance to your needs.**

## Tasks

### 0. Debugging - Python Factorial
*   **Objective:** Use ChatGPT to identify and correct errors in code samples.
*   **Code:**
    ```python
    #!/usr/bin/python3
    import sys

    def factorial(n):
        result = 1
        while n > 1:
            result *= n
            n -= 1
        return result

    f = factorial(int(sys.argv[1]))
    print(f)
    ```
*   **File:** `debugging/factorial.py`
*   **Repository:** `holbertonschool-chatgpt-introduction`
*   **Description:** The provided code calculates the factorial of a number. Fix the errors in this python script so it calculates the factorial of the number in arguments.

### 1. Debugging - Python Arguments
*   **Objective:** Use ChatGPT to identify and correct errors in code samples.
*   **Code:**
    ```python
    #!/usr/bin/python3
    import sys

    for i in range(1, len(sys.argv)):
        print(sys.argv[i])
    ```
*   **File:** `debugging/print_arguments.py`
*   **Repository:** `holbertonschool-chatgpt-introduction`
*   **Description:** The provided script prints the arguments passed to it including the script name. Fix the code to print only the arguments without the script's file name.

### 2. Debugging - HTML / Javascript
*   **Objective:** Use ChatGPT to identify and correct errors in code samples.
*   **Code:**
    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Change Background Color</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                text-align: center;
                padding-top: 50px;
            }
            button {
                padding: 10px 20px;
                font-size: 16px;
                cursor: pointer;
            }
        </style>
    </head>
    <body>

        <h2>Click the button to change the background color</h2>

        <button id="colorButton">Change Color</button>

        <script>
            document.getElementById("colorButton").addEventListener("click", function() {
                changeBackgroundColor();
            });

            function changeBackgroundColor() {
                // Generate a random color
                var randomColor = "#" + Math.floor(Math.random()*16777215).toString(16);
                // Change the background color of the body
                document.body.style.backgroundColor = randomColor;
            }
        </script>

    </body>
    </html>
    ```
*   **File:** `debugging/change_background.html`
*   **Repository:** `holbertonschool-chatgpt-introduction`
*   **Description:** The provided HTML/Javascript should change the background color when the button is clicked. Fix the code to make the functionality work.

### 3. Debugging - Python Mines
*   **Objective:** Use ChatGPT to identify and correct errors in code samples.
*   **Code:**
    ```python
    #!/usr/bin/python3
    import random
    import os

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    class Minesweeper:
        def __init__(self, width=10, height=10, mines=10):
            self.width = width
            self.height = height
            self.mines = set(random.sample(range(width * height), mines))
            self.field = [[' ' for _ in range(width)] for _ in range(height)]
            self.revealed = [[False for _ in range(width)] for _ in range(height)]
            self.unrevealed_count = width * height - mines

        def print_board(self, reveal=False):
            clear_screen()
            print('  ' + ' '.join(str(i) for i in range(self.width)))
            for y in range(self.height):
                print(y, end=' ')
                for x in range(self.width):
                    if reveal or self.revealed[y][x]:
                        if (y * self.width + x) in self.mines:
                            print('*', end=' ')
                        else:
                            count = self.count_mines_nearby(x, y)
                            print(count if count > 0 else ' ', end=' ')
                    else:
                        print('.', end=' ')
                print()

        def count_mines_nearby(self, x, y):
            count = 0
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.width and 0 <= ny < self.height:
                        if (ny * self.width + nx) in self.mines:
                            count += 1
            return count

        def reveal(self, x, y):
            if (y * self.width + x) in self.mines:
                return False
            if not self.revealed[y][x]:
                self.revealed[y][x] = True
                self.unrevealed_count -= 1
                if self.count_mines_nearby(x, y) == 0:
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            nx, ny = x + dx, y + dy
                            if 0 <= nx < self.width and 0 <= ny < self.height and not self.revealed[ny][nx]:
                                self.reveal(nx, ny)
            return True
        
        def check_win(self):
            return self.unrevealed_count == 0
            

        def play(self):
            while True:
                self.print_board()
                if self.check_win():
                    print("Congratulations! You've won the game.")
                    break
                try:
                    x = int(input("Enter x coordinate: "))
                    y = int(input("Enter y coordinate: "))
                    if not self.reveal(x, y):
                        self.print_board(reveal=True)
                        print("Game Over! You hit a mine.")
                        break
                except ValueError:
                    print("Invalid input. Please enter numbers only.")

    if __name__ == "__main__":
        game = Minesweeper()
        game.play()
    ```
*   **File:** `debugging/mines.py`
*   **Repository:** `holbertonschool-chatgpt-introduction`
*   **Description:** The provided code implements a Minesweeper game. Fix the code to detect when all non-mine cells have been revealed and notify the user of the win.

### 4. Documentation - Python Factorial
*   **Objective:** Use ChatGPT to document the code.
*   **Code:**
    ```python
    #!/usr/bin/python3
    import sys

    def factorial(n):
        """
        Calculate the factorial of a non-negative integer.

        Args:
            n (int): The non-negative integer for which to calculate the factorial.

        Returns:
            int: The factorial of n.
        """
        if n == 0:
            return 1
        else:
            return n * factorial(n-1)

    f = factorial(int(sys.argv[1]))
    print(f)
    ```
*   **File:** `debugging/factorial_recursive.py`
*   **Repository:** `holbertonschool-chatgpt-introduction`
*   **Description:** The provided script calculates a factorial recursively.  Add the comments to this code using a function description, parameters and returns.

### 5. Error Handling - Python Checkbook
*   **Objective:** Use ChatGPT to add error handling to the code.
*   **Code:**
    ```python
    class Checkbook:
        def __init__(self):
            self.balance = 0.0

        def deposit(self, amount):
            self.balance += amount
            print("Deposited ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

        def withdraw(self, amount):
            if amount > self.balance:
                print("Insufficient funds to complete the withdrawal.")
            else:
                self.balance -= amount
                print("Withdrew ${:.2f}".format(amount))
                print("Current Balance: ${:.2f}".format(self.balance))

        def get_balance(self):
            print("Current Balance: ${:.2f}".format(self.balance))

    def main():
        cb = Checkbook()
        while True:
            action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
            if action.lower() == 'exit':
                break
            elif action.lower() == 'deposit':
                while True:
                    try:
                        amount = float(input("Enter the amount to deposit: $"))
                        cb.deposit(amount)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
            elif action.lower() == 'withdraw':
                while True:
                    try:
                        amount = float(input("Enter the amount to withdraw: $"))
                        cb.withdraw(amount)
                        break
                    except ValueError:
                        print("Invalid input. Please enter a valid number.")
            elif action.lower() == 'balance':
                cb.get_balance()
            else:
                print("Invalid command. Please try again.")

    if __name__ == "__main__":
        main()
    ```
*   **File:** `debugging/checkbook.py`
*   **Repository:** `holbertonschool-chatgpt-introduction`
*   **Description:** The checkbook script doesn't have error handling for incorrect user input. Update the script to prevent it from crashing due to non-numeric input.

### 6. Debugging - Tic Tac Toe Python
*  **Objective:** Use ChatGPT to identify and correct errors in code samples.
*   **Code:**
    ```python
    #!/usr/bin/python3
    def print_board(board):
        for row in board:
            print(" | ".join(row))
            print("-" * 5)

    def check_winner(board):
        for row in board:
            if row.count(row[0]) == len(row) and row[0] != " ":
                return True

        for col in range(len(board[0])):
            if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
                return True

        if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
            return True

        if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
            return True

        return False

    def tic_tac_toe():
        board = [[" "]*3 for _ in range(3)]
        player = "X"
        moves = 0
        while True:
            print_board(board)
            try:
                row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
                col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
                if 0 <= row <= 2 and 0 <= col <= 2:
                    if board[row][col] == " ":
                        board[row][col] = player
                        moves += 1
                        if check_winner(board):
                            print_board(board)
                            print("Player " + player + " wins!")
                            break
                        if moves == 9:
                            print_board(board)
                            print("It's a draw!")
                            break
                        player = "O" if player == "X" else "X"

                    else:
                        print("That spot is already taken! Try again.")
                else:
                    print("Invalid row or column, please use the values 0, 1 or 2")
            except ValueError:
                print("Invalid input, please enter numbers.")


    tic_tac_toe()
    ```
*   **File:** `debugging/tic.py`
*   **Repository:** `holbertonschool-chatgpt-introduction`
*   **Description:** The provided Tic Tac Toe game has some bugs and doesn't handle all the user inputs. Fix the script to allow playing the game correctly.
