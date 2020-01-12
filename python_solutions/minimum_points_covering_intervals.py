import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals):
    intervals.sort(key=lambda x: x.right)
    prev_right = float('-inf')
    total = 0
    for interval in intervals:
        if interval.left > prev_right:
            prev_right = interval.right
            total += 1
    return total


@enable_executor_hook
def find_minimum_visits_wrapper(executor, A):
    A = [Interval(*a) for a in A]
    return executor.run(functools.partial(find_minimum_visits, A))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_points_covering_intervals.py",
                                       'minimum_points_covering_intervals.tsv',
                                       find_minimum_visits_wrapper))
