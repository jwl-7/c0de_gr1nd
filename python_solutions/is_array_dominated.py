import collections
import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


class Team:
    Player = collections.namedtuple('Player', ('height'))

    def __init__(self, height):
        self.players = [Team.Player(h) for h in height]

    @staticmethod
    def valid_placement_exists(team0, team1):
        team0.players.sort()
        team1.players.sort()
        return all(x < y for x, y in zip(team0.players, team1.players))


@enable_executor_hook
def valid_placement_exists_wrapper(executor, team0, team1, expected_01,
                                   expected_10):
    t0, t1 = Team(team0), Team(team1)

    result_01 = executor.run(
        functools.partial(Team.valid_placement_exists, t0, t1))
    result_10 = executor.run(
        functools.partial(Team.valid_placement_exists, t1, t0))
    if result_01 != expected_01 or result_10 != expected_10:
        raise TestFailure("")


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_array_dominated.py",
                                       'is_array_dominated.tsv',
                                       valid_placement_exists_wrapper))
