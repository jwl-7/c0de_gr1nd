# Reconstruct a BST from Traversal Data
Given a preorder sequence, reconstruct the BST.

## Example
```
 Input: preorder = [4, 2, 1, 3, 5]
Output:

        4
       / \
      2   5
     / \
    1   3
```

## Solution
```python
def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None

    root = BinaryTreeNode(preorder_sequence[0])
    i = 1
    while i < len(preorder_sequence):
        if preorder_sequence[i] < preorder_sequence[0]:
            i += 1
        else:
            break

    root.left = rebuild_bst_from_preorder(preorder_sequence[1:i])
    root.right = rebuild_bst_from_preorder(preorder_sequence[i:])
    return root
```

## Explanation
* BLANK

## Code Dissection
1. BLANK