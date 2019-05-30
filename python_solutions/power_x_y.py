from test_framework import generic_test


def power(x, y):
    result = 1
    if y < 0:
        y = -y
        x = 1 / x
    while y:
        if y & 1:
            result *= x
        x *= x
        y >>= 1
    return result


if __name__ == '__main__':
    exit(generic_test.generic_test_main("power_x_y.py", 'power_x_y.tsv', power))