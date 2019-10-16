from test_framework import generic_test


def evaluate(expression):
    stack = []
    operators = '+-*/'
    for token in expression.split(','):
        if token not in operators:
            stack.append(int(token))
        else:
            y = stack.pop()
            x = stack.pop()
            if token == '+':
                result = x + y
            elif token == '-':
                result = x - y
            elif token == '*':
                result = x * y
            elif token == '/':
                result = int(x / y)
            stack.append(result)
    return stack[0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("evaluate_rpn.py", 'evaluate_rpn.tsv',
                                       evaluate))
