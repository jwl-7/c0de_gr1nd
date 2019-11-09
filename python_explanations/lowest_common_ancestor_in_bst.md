# Compute the LCA in a BST
Given two nodes _s_ and _b_ in a BST, find the lowest common ancestor. _s_ <= _b_

## Example
```
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