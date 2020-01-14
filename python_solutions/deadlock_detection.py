import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook


class GraphVertex:

    WHITE, GRAY, BLACK = range(3)

    def __init__(self):
        self.color = GraphVertex.WHITE
        self.edges = []


def is_deadlocked(graph):
    def has_cycle(curr):
        if curr.color == GraphVertex.GRAY:
            return True

        curr.color = GraphVertex.GRAY

        for nxt in curr.edges:
            if nxt.color != GraphVertex.BLACK and has_cycle(nxt):
                return True

        curr.color = GraphVertex.BLACK
        return False

    for vertex in graph:
        if vertex.color == GraphVertex.WHITE and has_cycle(vertex):
            return True
    return False


@enable_executor_hook
def is_deadlocked_wrapper(executor, num_nodes, edges):
    if num_nodes <= 0:
        raise RuntimeError('Invalid num_nodes value')
    graph = [GraphVertex() for _ in range(num_nodes)]

    for (fr, to) in edges:
        if fr < 0 or fr >= num_nodes or to < 0 or to >= num_nodes:
            raise RuntimeError('Invalid vertex index')
        graph[fr].edges.append(graph[to])

    return executor.run(functools.partial(is_deadlocked, graph))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("deadlock_detection.py",
                                       'deadlock_detection.tsv',
                                       is_deadlocked_wrapper))
