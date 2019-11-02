import itertools

from test_framework import generic_test
from test_framework.test_failure import TestFailure


def find_missing_element(stream):
    block_size = 1 << 16
    stream, stream_copy = itertools.tee(stream)

    count_block = [0] * block_size
    for ip in stream:
        count_block[ip // block_size] += 1

    block_idx = 0
    for i, val in enumerate(count_block):
        if val < block_size:
            block_idx = i
            break

    block = [0] * block_size
    stream = stream_copy
    for ip in stream_copy:
        if ip // block_size == block_idx:
            block[ip % block_size] = 1

    for i, val in enumerate(block):
        if not val:
            return block_idx * block_size + i


def find_missing_element_wrapper(data):
    try:
        return find_missing_element(iter(data))
    except ValueError:
        raise TestFailure('Unexpected no_missing_element exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("absent_value_array.py",
                                       'absent_value_array.tsv',
                                       find_missing_element_wrapper))
