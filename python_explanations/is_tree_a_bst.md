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
* BLANK

## Code Dissection
1. BLANK