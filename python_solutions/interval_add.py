import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import PropertyName
from test_framework.test_utils import enable_executor_hook


Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    i = 0
    n = len(disjoint_intervals)
    merged = []
    while i < n and disjoint_intervals[i].right < new_interval.left:
        merged.append(disjoint_intervals[i])
        i += 1
    while i < n and disjoint_intervals[i].left <= new_interval.right:
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right)
        )
        i += 1
    merged.append(new_interval)
    merged += disjoint_intervals[i:]
    return merged


@enable_executor_hook
def add_interval_wrapper(executor, disjoint_intervals, new_interval):
    disjoint_intervals = [Interval(*x) for x in disjoint_intervals]
    return executor.run(
        functools.partial(add_interval, disjoint_intervals,
                          Interval(*new_interval)))


def res_printer(prop, value):
    def fmt(x):
        return [[e[0], e[1]] for e in x] if x else None

    if prop in (PropertyName.EXPECTED, PropertyName.RESULT):
        return fmt(value)
    else:
        return value


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "interval_add.py",
            'interval_add.tsv',
            add_interval_wrapper,
            res_printer=res_printer))
