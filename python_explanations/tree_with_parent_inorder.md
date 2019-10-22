# Implement an Inorder Traversal with _O(1)_ Space
The direct implementation of an inorder traversal using recursion has _O(h)_ space complexity, where _h_ is the height of the tree. Recursion can be removed with an explicit stack, but the space complexity remains _O(h)_.

Write a nonrecursive program for computing the inorder traversal sequence for a binary tree. Assume nodes have parent fields.

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
    result = []
    while tree and tree.left:
        tree = tree.left
    while tree:
        result.append(tree.data)
        if tree.right:
            tree = tree.right
            while tree.left:
                tree = tree.left
        else:
            while tree.parent and tree.parent.right is tree:
                tree = tree.parent
            tree = tree.parent
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK