import collections
import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:

    def __init__(self):
        self.color = -1
        self.edges = []


def is_any_placement_feasible(graph):
    def bfs(s):
        s.color = 0
        q = collections.deque([s])
        while q:
            curr = q.popleft()
            for v in curr.edges:
                if v.color == -1:
                    v.color = curr.color + 1
                    q.append(v)
                elif v.color == curr.color:
                    return False
        return True

    return all(bfs(v) for v in graph if v.color == -1)


@enable_executor_hook
def is_any_placement_feasible_wrapper(executor, k, edges):
    if k <= 0:
        raise RuntimeError('Invalid k value')
    graph = [GraphVertex() for _ in range(k)]

    for (fr, to) in edges:
        if fr < 0 or fr >= k or to < 0 or to >= k:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_any_placement_feasible, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_circuit_wirable.py",
                                       'is_circuit_wirable.tsv',
                                       is_any_placement_feasible_wrapper))
