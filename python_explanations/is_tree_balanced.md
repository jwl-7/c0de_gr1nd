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
* Given the definition of a balanced tree, a tree _T_ is not balanced if and only if there is some node _p_ in _T_ such that |height(_p.left_) - height(_p.right_)| > 1
* The solution recursively traverses the tree from the top -> down to see if any subtrees do not fit the definition of a balanced tree
* For this specific problem, the book treats an empty tree as a balanced tree
* The height for an empty tree = 0
* The height for an empty subtree = -1
* The height for a non-empty tree/subtree = (max(height(_p.left_), height(_p.right_))) + 1

## Code Dissection - height
1. If the _tree_ is empty, return the height as 0
    ```python
    if not tree:
        return 0
    ```
2. Check the left subtree's height
    ```python
    left = height(tree.left)
    if left == -1:
        return -1
    ```
3. Check the right subtree's height
    ```python
    right = height(tree.right)
    if right == -1 or abs(left - right) > 1:
        return -1
    ```
4. Return the current node's height
    ```python
    return max(left, right) + 1
    ```

## Code Dissection - is_balanced_binary_tree
1. Return whether or not the tree is height-balanced
    ```python
    return height(tree) != -1
    ```