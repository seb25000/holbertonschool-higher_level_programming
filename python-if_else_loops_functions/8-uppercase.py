#!/usr/bin/env python3

def uppercase(str):
    result = ""
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            result += chr(ord(char) - 32)
        else:
            result += char
    print("{}".format(result))
#!/usr/bin/env python3

uppercase("best")
uppercase("Best School 98 Battery street")
