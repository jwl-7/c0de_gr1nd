import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            weight = items[i-1].weight
            value = items[i-1].value
            if weight <= j:
                dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]


@enable_executor_hook
def optimum_subject_to_capacity_wrapper(executor, items, capacity):
    items = [Item(*i) for i in items]
    return executor.run(
        functools.partial(optimum_subject_to_capacity, items, capacity))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("knapsack.py", "knapsack.tsv",
                                       optimum_subject_to_capacity_wrapper))
