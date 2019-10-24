# Reconstruct a Binary Tree from a Preorder Traversal with Markers
Many different binary trees have the same preorder traversal sequence.

In this problem, the preorder traversal computation is modified to mark where a left or right child is empty.

Design an algorithm for reconstructing a binary tree from a preorder traversal visit sequence that uses _null_ to mark empty children.

## Example
```
 Input: preorder = [1, 2, 7, None, None, 5, None, None, 3, None, None]
Output:
            1
           / \
          2   3
         / \
        7   5
```

## Solution
```python
def reconstruct_preorder(preorder):
    def helper(preorder_iter):
        root = next(preorder_iter)
        if root is not None:
            left = helper(preorder_iter)
            right = helper(preorder_iter)
            return BinaryTreeNode(root, left, right)
    return helper(iter(preorder))
```

## Explanation
* BLANK

## Code Dissection
1. BLANK