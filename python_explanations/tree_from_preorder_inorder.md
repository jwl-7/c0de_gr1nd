# Reconstruct a Binary Tree from Traversal Data
Many different binary trees yield the same sequence of keys in an inorder, preorder, or postorder traversal. However, given an inorder traversal and one of any two other traversal orders of a binary tree, there exists a unique binary tree that yields those orders, assuming each node holds a distinct key.

Given an inorder traversal sequence and a preorder traversal sequence of a binary tree, write a program to reconstruct the tree. Assume each node has a unique key.

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
1. Check if the _inorder_ sequence is empty, in which case `None` is returned
    ```python
    if inorder:
    ```
    * This will be the case when a node does not have a left or right subtree
2. Get the first element in the _preorder_ sequence and find the index of that element in the _inorder_ sequence
    ```python
    idx = inorder.index(preorder.pop(0))
    ```
3. Create a _root_ node from the first element in the _preorder_ sequence
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