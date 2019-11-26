import functools

from test_framework import generic_test
from test_framework.test_utils import enable_executor_hook
from binary_tree_node import BinaryTreeNode


def generate_all_binary_trees(num_nodes):
    if not num_nodes:
        return [None]

    result = []
    for num_left in range(num_nodes):
        num_right = num_nodes - num_left - 1
        left_tree = generate_all_binary_trees(num_left)
        right_tree = generate_all_binary_trees(num_right)
        result += [
            BinaryTreeNode(0, left, right)
            for left in left_tree
            for right in right_tree
        ]
    return result


def serialize_structure(tree):
    result = []
    q = [tree]
    while q:
        a = q.pop(0)
        result.append(0 if not a else 1)
        if a:
            q.append(a.left)
            q.append(a.right)
    return result


@enable_executor_hook
def generate_all_binary_trees_wrapper(executor, num_nodes):
    result = executor.run(
        functools.partial(generate_all_binary_trees, num_nodes))

    return sorted(map(serialize_structure, result))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_trees.py",
                                       'enumerate_trees.tsv',
                                       generate_all_binary_trees_wrapper))
