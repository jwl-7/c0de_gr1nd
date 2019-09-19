from test_framework import generic_test


def convert_base(num_as_string, b1, b2):
    if num_as_string == '0' or num_as_string == '-0':
        return num_as_string

    is_negative = False
    if num_as_string[0] == '-':
        num_as_string = num_as_string[1:]
        is_negative = True

    num = 0
    for digit in num_as_string:
        num = num * b1 + int(digit, 16)
    
    digits = []
    while num > 0:
        digits.append(f'{int(num % b2):X}')
        num //= b2

    return ('-' if is_negative else '') + ''.join(digits[::-1])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("convert_base.py", "convert_base.tsv",
                                       convert_base))
