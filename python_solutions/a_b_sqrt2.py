from test_framework import generic_test
from sortedcontainers import SortedDict


class Number:

    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.val = a + b * (2 ** (1 / 2))


def generate_first_k_a_b_sqrt2(k):
    nums = SortedDict()
    nums[0.0] = Number(0, 0)
    result = []
    while len(result) < k:
        nxt = nums.popitem(0)[1]
        result.append(nxt.val)
        a = Number(nxt.a + 1, nxt.b)
        b = Number(nxt.a, nxt.b + 1)
        nums[a.val] = a
        nums[b.val] = b
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("a_b_sqrt2.py", 'a_b_sqrt2.tsv',
                                       generate_first_k_a_b_sqrt2))
