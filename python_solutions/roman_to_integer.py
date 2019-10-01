from test_framework import generic_test


def roman_to_integer(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev = 0
    for char in s[::-1]:
        if roman[char] < prev:
            result -= roman[char]
        else:
            result += roman[char]
        prev = roman[char]
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "roman_to_integer.py", 'roman_to_integer.tsv', roman_to_integer))
