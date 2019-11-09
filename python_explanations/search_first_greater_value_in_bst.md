# Find the First Key Greater Than a Given Value in a BST
Given a BST and a value _k_, return the first node in an inorder traversal greater than _k_.

## Example
```
        4
       / \
      2   5
     / \
    1   3

Inorder Traversal: [1, 2, 3, 4, 5]

 Input: k = 3
Output: 4
```

## Solution
```python
def find_first_greater_than_k(tree, k):
    result = None
    while tree:
        if tree.data > k:
            result = tree
            tree = tree.left
        else:
            tree = tree.right
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK