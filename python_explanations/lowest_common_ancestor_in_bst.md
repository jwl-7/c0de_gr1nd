# Compute the LCA in a BST
Given two nodes in a BST, find the lowest common ancestor.

## Example
```
s = node 1
b = node 2

        4
       / \
      2   5
     / \
    1   3

 Input: s = 1, b = 3
Output: 2
```

## Solution
```python
def find_LCA(tree, s, b):
    while not s.data <= tree.data <= b.data:
        if s.data < tree.data:
            tree = tree.left
        else:
            tree = tree.right
    return tree
```

## Explanation
* BLANK

## Code Dissection
1. BLANK