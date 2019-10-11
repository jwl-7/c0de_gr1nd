import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


# Assume s is a string encoded as bytearray.
def reverse_words(s):
    s[:] = s[::-1]
    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            if start == 0:
                s[:] = s[::-1]
            else:
                s[start:] = s[end:start-1:-1]
            break
        if start < end:
            if start == 0:
                s[start:end] = s[end-1::-1]
            else:
                s[start:end] = s[end-1:start-1:-1]
        start = end + 1


def reverse_words_pythonic(s):
    s[:] = b' '.join(word[::-1] for word in s[::-1].split(b' '))


@enable_executor_hook
def reverse_words_wrapper(executor, s):
    s_copy = bytearray()
    s_copy.extend(map(ord, s))

    executor.run(functools.partial(reverse_words, s_copy))

    return s_copy.decode("utf-8")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("reverse_words.py", 'reverse_words.tsv',
                                       reverse_words_wrapper))
