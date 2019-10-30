# Reconstruct a Binary Tree from a Preorder Traversal with Markers
Many different binary trees have the same preorder traversal sequence.

In this problem, the preorder traversal computation is modified to mark where a left or right child is empty.

Design an algorithm for reconstructing a binary tree from a preorder traversal visit sequence that uses _null_ to mark empty children.

## Example
```
 Input: preorder = [1, 2, 7, null, null, 5, null, null, 3, null, null]
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
        if root:
            left = helper(preorder_iter)
            right = helper(preorder_iter)
            return BinaryTreeNode(root, left, right)
    return helper(iter(preorder))
```

## Explanation
* The null markers in the preorder sequence help determine which nodes belong to the left and right subtrees of a root
* To put it another way, the null markers tell us when a right subtree begins, which provides a good base case for the solution's algorithm

## Code Dissection - reconstruct_preorder
1. Send an iterator made from the preorder sequence to the helper function and return the reconstructed binary tree
    ```python
    return helper(iter(preorder))
    ```

## Code Dissection - helper
1. Set the root value of the subtree as the next element in the preorder sequence
    ```python
    root = next(preorder_iter)
    ```
2. If the next element in the preorder sequence is not null, then process the left and right subtrees for _root_
    ```python
    if root:
        left = helper(preorder_iter)
        right = helper(preorder_iter)
        return BinaryTreeNode(root, left, right)