from test_framework import generic_test


def binary_tree_depth_order(tree):
    result = []
    level = [tree]
    while tree and level:
        curr_nodes = []
        next_level = []
        for node in level:
            curr_nodes.append(node.data)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        result.append(curr_nodes)
        level = next_level
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_level_order.py",
                                       "tree_level_order.tsv",
                                       binary_tree_depth_order))
