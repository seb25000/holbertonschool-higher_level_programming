#!/usr/bin/python3

def uppercase(str):
    """Converts a string to uppercase."""
    result = ""
    for char in str:
        if 'a' <= char <= 'z':
            uppercase_char = chr(ord(char) - 32)  # Convert lowercase to uppercase
        else:
            uppercase_char = char  # Keep non-lowercase chars unchanged
        result += uppercase_char
    print("{}".format(result))


if __name__ == "__main__":
    # Example usage
    uppercase("hello world")  # Output: HELLO WORLD
    uppercase("python is fun")  # Output: PYTHON IS FUN
    uppercase("123abcDEF!")     # Output: 123ABCDEF!
    uppercase("This Is Mixed")   # Output: THIS IS MIXED
    uppercase("") #Output:
