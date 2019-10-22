from test_framework import generic_test


def inorder_traversal(tree):
    result = []
    while tree and tree.left:
        tree = tree.left
    while tree:
        result.append(tree.data)
        if tree.right:
            tree = tree.right
            while tree.left:
                tree = tree.left
        else:
            while tree.parent and tree.parent.right is tree:
                tree = tree.parent
            tree = tree.parent
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("tree_with_parent_inorder.py",
                                       'tree_with_parent_inorder.tsv',
                                       inorder_traversal))
