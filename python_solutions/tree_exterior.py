import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def exterior_binary_tree(tree):

    def left_boundary(tree):
        if not tree or (not tree.left and not tree.right):
            return
        exterior.append(tree)
        if tree.left:
            left_boundary(tree.left)
        else:
            left_boundary(tree.right)

    def right_boundary(tree):
        if not tree or (not tree.left and not tree.right):
            return
        if tree.right:
            right_boundary(tree.right)
        else:
            right_boundary(tree.left)
        exterior.append(tree)

    def leaves(tree):
        if not tree:
            return
        if not tree.left and not tree.right:
            exterior.append(tree)
            return
        leaves(tree.left)
        leaves(tree.right)

    if not tree:
        return []

    exterior = [tree]
    left_boundary(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    right_boundary(tree.right)
    return exterior


def create_output_list(L):
    if any(l is None for l in L):
        raise TestFailure('Resulting list contains None')
    return [l.data for l in L]


@enable_executor_hook
def create_output_list_wrapper(executor, tree):
    result = executor.run(functools.partial(exterior_binary_tree, tree))

    return create_output_list(result)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_exterior.py", 'tree_exterior.tsv',
                                       create_output_list_wrapper))
