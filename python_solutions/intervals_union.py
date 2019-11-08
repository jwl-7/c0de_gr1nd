import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))
Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    intervals.sort(key=lambda x: (x.left.val, not x.left.is_closed))
    union = [intervals[0]]
    for curr in intervals:
        prev = union[-1]
        if (
            curr.left.val < prev.right.val or
            curr.left.val == prev.right.val and
            (curr.left.is_closed or prev.right.is_closed)
        ):
            if (
                curr.right.val > prev.right.val or
                curr.right.val == prev.right.val and
                curr.right.is_closed
            ):
                union[-1] = Interval(prev.left, curr.right)
        else:
            union.append(curr)
    return union


@enable_executor_hook
def union_of_intervals_wrapper(executor, intervals):
    intervals = [
        Interval(Endpoint(x[1], x[0]), Endpoint(x[3], x[2])) for x in intervals
    ]

    result = executor.run(functools.partial(union_of_intervals, intervals))

    return [(i.left.val, i.left.is_closed, i.right.val, i.right.is_closed)
            for i in result]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("intervals_union.py",
                                       "intervals_union.tsv",
                                       union_of_intervals_wrapper))
