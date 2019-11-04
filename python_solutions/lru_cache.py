import collections

from test_framework import generic_test
from test_framework.test_failure import TestFailure


class LruCache:

    def __init__(self, capacity):
        self.prices = collections.OrderedDict()
        self.capacity = capacity

    def lookup(self, isbn):
        if isbn not in self.prices:
            return -1
        self.prices.move_to_end(isbn, last=False)
        return self.prices[isbn]

    def insert(self, isbn, price):
        if isbn not in self.prices:
            if len(self.prices) == self.capacity:
                self.prices.popitem()
            self.prices[isbn] = price
        self.prices.move_to_end(isbn, last=False)

    def erase(self, isbn):
        return self.prices.pop(isbn, False) is not False


def run_test(commands):
    if len(commands) < 1 or commands[0][0] != 'LruCache':
        raise RuntimeError('Expected LruCache as first command')

    cache = LruCache(commands[0][1])

    for cmd in commands[1:]:
        if cmd[0] == 'lookup':
            result = cache.lookup(cmd[1])
            if result != cmd[2]:
                raise TestFailure(
                    'Lookup: expected ' + str(cmd[2]) + ', got ' + str(result))
        elif cmd[0] == 'insert':
            cache.insert(cmd[1], cmd[2])
        elif cmd[0] == 'erase':
            result = 1 if cache.erase(cmd[1]) else 0
            if result != cmd[2]:
                raise TestFailure(
                    'Erase: expected ' + str(cmd[2]) + ', got ' + str(result))
        else:
            raise RuntimeError('Unexpected command ' + cmd[0])


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("lru_cache.py", 'lru_cache.tsv',
                                       run_test))
