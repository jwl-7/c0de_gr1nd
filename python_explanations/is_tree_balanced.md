# Test If a Binary Tree Is Height-Balanced
Given a binary tree, determine whether or not it is height-balanced. A height-balanced tree is a binary tree in which the left and right subtrees of every node differ in height by at most 1.

## Examples
```
      3
     / \
    7  12
       / \
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
* The solution uses a postorder traversal (bottum-up recursion) to check if the child subtrees are balanced before comparing their heights
* For this specific problem, the book treats an empty tree as a balanced tree
* The height for an empty tree = 0
* The height for an empty subtree = -1
* The height for a non-empty tree/subtree = (max(height(_p.left_), height(_p.right_))) + 1

## Code Dissection - height
1. If the tree is empty, return the height as 0
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