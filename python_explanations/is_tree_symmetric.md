# Test If a Binary Tree Is Symmetric
A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree is the mirror image of the right subtree.

Write a program that checks whether a binary tree is symmetric.

## Examples
```
    1
   / \
  2   2
 / \ / \
3  4 4  3

 Input: [1, 2, 2, 3, 4, 4, 3]
Output: True


    1
   / \
  2   2
   \   \
   3    3

 Input: [1, 2, 2, null, 3, null, 3]
Output: False
```

## Solution
```python
def is_mirror(n1, n2):
    if not n1 and not n2:
        return True
    elif n1 and n2 and n1.data == n2.data:
        return is_mirror(n1.right, n2.left) and is_mirror(n1.left, n2.right)
    return False


def is_symmetric(tree):
    return is_mirror(tree, tree)
```

## Explanation
* BLANK

## Code Dissection
1. BLANK