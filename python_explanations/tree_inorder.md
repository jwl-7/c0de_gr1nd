# Implement an Inorder Traversal Without Recursion
Write a program which takes as input a binary tree and performs an inorder traversal of the tree. Do not use recursion. Nodes do not contain parent references.

## Example
```
       1
      / \
     2   3
    / \
   7   5

 Input: [1, 2, 3, 7, 5, null, null]
Output: [7, 2, 5, 1, 3]
```

## Solution
```python
def inorder_traversal(tree):
    stack = []
    result = []
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            result.append(tree.data)
            tree = tree.right
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK