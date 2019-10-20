# Test If a Binary Tree Is Height-Balanced
A binary tree is said to be height-balanced if for each node in the tree, the difference in the height of its left and right subtrees is at most one. A perfect binary tree is height-balanced, as is a complete binary tree. A height-balanced binary tree does not have to be perfect or complete.

Write a program that takes as input the root of a binary tree and checks whether the tree is height-balanced.

## Examples
```
    3
   / \
  7  12
    /  \
   11   9

 Input: [3, 7, 12, null, null, 11, 9]
Output: True


       1
      / \
     2   3
    / \
   7   5
  / \
 6   11

 Input: [1, 2, 3, 7, 5, null, null, 6, 11]
Output: False
```

## Solution
```python
def height(tree):
    if not tree:
        return 0

    left = height(tree.left)
    if left == -1:
        return -1

    right = height(tree.right)
    if right == -1 or abs(left - right) > 1:
        return -1

    return max(left, right) + 1


def is_balanced_binary_tree(tree):
    return height(tree) != -1
```

## Explanation
* BLANK

## Code Dissection
1. BLANK