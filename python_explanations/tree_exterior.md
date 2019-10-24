# Compute the Exterior of a Binary Tree
The exterior of a binary tree is the following sequence of nodes: the nodes from the root to the leftmost leaf, followed by the leaves in left-to-right order, followed by the nodes from the rightmost leaf to the root.

Write a program that computes the exterior of a binary tree.

## Example
```
        3
       / \
      5   1
     / \   \
    6   2   8
       / \
      9   4

 Input: [3, 5, 1, 6, 2, null, 8, null, null, 9, 4, null, null]
Output: [3, 5, 6, 9, 4, 8, 1]
```

## Solution
```python
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
```

## Explanation
* BLANK

## Code Dissection
1. BLANK