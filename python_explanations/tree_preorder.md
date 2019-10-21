# Implement a Preorder Traversal Without Recursion
Write a program which takes as input a binary tree and performs a preorder traversal of the tree. Do not use recursion. Nodes do not contain parent references.

## Example
```
       1
      / \
     2   3
    / \
   7   5

 Input: [1, 2, 3, 7, 5, null, null]
Output: [1, 2, 7, 5, 3]
```

## Solution
```python
def preorder_traversal(tree):
    stack = []
    result = []
    while stack or tree:
        if tree:
            stack.append(tree)
            result.append(tree.data)
            tree = tree.left
        else:
            tree = stack.pop()
            tree = tree.right
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK