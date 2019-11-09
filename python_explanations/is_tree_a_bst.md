# Test If a Binary Tree Satisfies the BST Property
Given a binary tree, check if it is a binary search tree.

## Examples
```
      2
     / \
    1   3

Input: [2, 1, 3]
Output: True


      7
     / \
    1   4
       / \
      3   5

 Input: [7, 1, 4, null, null, 3, 5]
Output: False
```

## Solution
```python
def is_binary_tree_bst(tree, low=float('-inf'), high=float('inf')):
    if not tree:
        return True

    return (
        low <= tree.data <= high and
        is_binary_tree_bst(tree.left, low, tree.data) and
        is_binary_tree_bst(tree.right, tree.data, high)
    )
```

## Explanation
* For any root, every node in its left subtree must be <= the key at the root
* For any root, every node in its right subtree must be >= the key at the root
* The nodes in the left subtree must be in the range [_low_ -> _root_]
* The nodes in the right subtree must be in the range [_root_ -> _high_]

## Code Dissection
1. Base case: stop recursing once we hit the end of a subtree
    ```python
    if not tree:
        return True
    ```
2. Validate the tree and return True/False
    ```python
    return (
        low <= tree.data <= high and
        is_binary_tree_bst(tree.left, low, tree.data) and
        is_binary_tree_bst(tree.right, tree.data, high)
    )
    ```
    1. `low <= tree.data <= high` check if the root is between the _low_ and _high_ range
    2. `(tree.left, low, tree.data)` check if the nodes in the left subtree are in the range [_low_ -> _root_]
    3. `(tree.right, tree.data, high)` check if the nodes in the right subtree are in the range [_root_ -> _high_]