import functools

from test_framework import generic_test
from test_framework.binary_tree_utils import must_find_node
from test_framework.test_utils import enable_executor_hook


def pair_includes_ancestor_and_descendant_of_m(node0, node1, middle):
    a = node0
    b = node1
    while (
        a is not node1 and
        a is not middle and
        b is not node0 and
        b is not middle and
        (a or b)
    ):
        if a:
            a = a.left if a.data > middle.data else a.right
        if b:
            b = b.left if b.data > middle.data else b.right

    if (
        a is not middle and
        b is not middle or
        a is node1 or
        b is node0
    ):
        return False

    return search_bst(middle, node1 if a is middle else node0)


def search_bst(tree, node):
    while tree and tree is not node:
        tree = tree.left if tree.data > node.data else tree.right
    return tree is node


@enable_executor_hook
def pair_includes_ancestor_and_descendant_of_m_wrapper(
        executor, tree, possible_anc_or_desc_0, possible_anc_or_desc_1,
        middle_idx):
    candidate0 = must_find_node(tree, possible_anc_or_desc_0)
    candidate1 = must_find_node(tree, possible_anc_or_desc_1)
    middle_node = must_find_node(tree, middle_idx)

    return executor.run(
        functools.partial(pair_includes_ancestor_and_descendant_of_m,
                          candidate0, candidate1, middle_node))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "descendant_and_ancestor_in_bst.py",
            'descendant_and_ancestor_in_bst.tsv',
            pair_includes_ancestor_and_descendant_of_m_wrapper))
