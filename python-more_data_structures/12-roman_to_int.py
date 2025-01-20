#!/usr/bin/python3
def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    # Dictionary mapping Roman numerals to integers
    roman_map = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    length = len(roman_string)

    # Iterate over the Roman string
    for i in range(length):
        # Get the current numeral value
        current_value = roman_map.get(roman_string[i], 0)

        # If not the last numeral and the next numeral is larger, subtract current value
        if i + 1 < length:
            next_value = roman_map.get(roman_string[i + 1], 0)
            if current_value < next_value:
                total -= current_value
            else:
                total += current_value
        else:
            total += current_value

    return total
