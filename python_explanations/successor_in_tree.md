# Compute the Successor
The successor of a node in a binary tree is the node that appears immediately after the given node in an inorder traversal.

Design an algorithm that computes the successor of a node in a binary tree. Assume that each node stores its parent.

## Example
```
       1
      / \
     2   3
    / \
   7   5

Inorder Traversal: [7, 2, 5, 1, 3]

 Input: 5
Output: 2
```

## Solution
```python
if node.right:
    node = node.right
    while node.left:
        node = node.left
    return node

while node.parent and node.parent.right is node:
    node = node.parent
return node.parent
```

## Explanation
* BLANK

## Code Dissection
1. BLANK