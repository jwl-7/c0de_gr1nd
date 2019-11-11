import collections

from test_framework import generic_test


Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree, interval):
    def helper(tree):
        if tree:
            if interval.left < tree.data:
                helper(tree.left)
            if interval.left <= tree.data <= interval.right:
                result.append(tree.data)
            if interval.right > tree.data:
                helper(tree.right)

    result = []
    helper(tree)
    return result


def range_lookup_in_bst_wrapper(tree, i):
    return range_lookup_in_bst(tree, Interval(*i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("range_lookup_in_bst.py",
                                       'range_lookup_in_bst.tsv',
                                       range_lookup_in_bst_wrapper))
