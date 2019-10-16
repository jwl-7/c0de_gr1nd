from test_framework import generic_test


def is_well_formed(s):
    stack = []
    brackets = {
        '[': ']',
        '(': ')',
        '{': '}'
    }
    for char in s:
        if char in brackets:
            stack.append(char)
        elif not stack or char != brackets[stack.pop()]:
            return False
    return not stack


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_parenthesization.py",
                                       'is_valid_parenthesization.tsv',
                                       is_well_formed))
