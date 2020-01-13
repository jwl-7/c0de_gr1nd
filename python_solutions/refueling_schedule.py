import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


MPG = 20


def find_ample_city(gallons, distances):
    start = 0
    gas = 0
    for i in range(len(gallons)):
        gas += gallons[i] - distances[i] // MPG
        if gas < 0:
            start = i + 1
            gas = 0
    return start


@enable_executor_hook
def find_ample_city_wrapper(executor, gallons, distances):
    result = executor.run(
        functools.partial(find_ample_city, gallons, distances))
    num_cities = len(gallons)
    tank = 0
    for i in range(num_cities):
        city = (result + i) % num_cities
        tank += gallons[city] * MPG - distances[city]
        if tank < 0:
            raise TestFailure('Out of gas on city {}'.format(i))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("refueling_schedule.py",
                                       'refueling_schedule.tsv',
                                       find_ample_city_wrapper))
