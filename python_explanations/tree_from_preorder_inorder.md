# Reconstruct a Binary Tree from Traversal Data
Given a preorder and inorder sequence, reconstruct the binary tree.

## Example
```
 Input: preorder = [1, 2, 7, 5, 3]
         inorder = [7, 2, 5, 1, 3]
Output:
            1
           / \
          2   3
         / \
        7   5
```

## Solution
```python
def binary_tree_from_preorder_inorder(preorder, inorder):
    if inorder:
        idx = inorder.index(preorder.pop(0))
        root = BinaryTreeNode(inorder[idx])
        root.left = binary_tree_from_preorder_inorder(preorder, inorder[:idx])
        root.right = binary_tree_from_preorder_inorder(preorder, inorder[idx+1:])
        return root
```

## Explanation
1. The preorder sequence is used to figure out the root element at each recursive step
2. Using the root element from the preorder sequence, the inorder sequence is split into nodes that lie in the left and right subtree respectively
3. The solution recurses until the tree is finished processing

## Code Dissection
1. Check if the inorder sequence is empty, in which case None is returned
    ```python
    if inorder:
    ```
    * This will be the case when a node does not have a left or right subtree
2. Get the first element in the preorder sequence and find the index of that element in the inorder sequence
    ```python
    idx = inorder.index(preorder.pop(0))
    ```
3. Create a root node from the first element in the preorder sequence
    ```python
    root = BinaryTreeNode(inorder[idx])
    ```
4. Create the left subtree
    ```python
    root.left = binary_tree_from_preorder_inorder(preorder, inorder[:idx])
    ```
5. Create the right subtree
    ```python
    root.right = binary_tree_from_preorder_inorder(preorder, inorder[idx+1:])
    ```
6. Return the (sub)tree
    ```python
    return root
    ```