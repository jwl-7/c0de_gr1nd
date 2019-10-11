from test_framework import generic_test


def remove_leading_zeroes(num):
    i = 0
    length = len(num) - 1
    while i < length and num[0] == 0:
        num.remove(0)
        i += 1
    return num


def multiply(num1, num2):
    negative = False
    if num1[0] < 0 or num2[0] < 0:
        negative = True
        if num1[0] < 0 and num2[0] < 0:
            negative = False
        num1[0] = abs(num1[0])
        num2[0] = abs(num2[0])

    product = [0] * len(num1 + num2)
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            product[i + j + 1] += num1[i] * num2[j]
            product[i + j] += product[i + j + 1] // 10
            product[i + j + 1] %= 10

    product = remove_leading_zeroes(product)
    if negative:
        product[0] = -product[0]
    return product


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("int_as_array_multiply.py",
                                       'int_as_array_multiply.tsv', multiply))
