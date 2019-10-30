# Compute the Exterior of a Binary Tree
The exterior of a binary tree is the following sequence of nodes: the nodes from the root to the leftmost leaf, followed by the leaves in left-to-right order, followed by the nodes from the rightmost leaf to the root.

Write a program that computes the exterior of a binary tree.

## Example
```
        3
       / \
      5   1
     / \   \
    6   2   8
       / \
      9   4

 Input: [3, 5, 1, 6, 2, null, 8, null, null, 9, 4, null, null]
Output: [3, 5, 6, 9, 4, 8, 1]
```

## Solution
```python
def exterior_binary_tree(tree):

    def left_boundary(tree):
        if not tree or (not tree.left and not tree.right):
            return
        exterior.append(tree)
        if tree.left:
            left_boundary(tree.left)
        else:
            left_boundary(tree.right)

    def right_boundary(tree):
        if not tree or (not tree.left and not tree.right):
            return
        if tree.right:
            right_boundary(tree.right)
        else:
            right_boundary(tree.left)
        exterior.append(tree)

    def leaves(tree):
        if not tree:
            return
        if not tree.left and not tree.right:
            exterior.append(tree)
            return
        leaves(tree.left)
        leaves(tree.right)

    if not tree:
        return []

    exterior = [tree]
    left_boundary(tree.left)
    leaves(tree.left)
    leaves(tree.right)
    right_boundary(tree.right)
    return exterior
```

## Explanation
1. Traverse the nodes in the left boundary [top -> down]
2. Traverse the leaf nodes in the left subtree [left -> right]
3. Traverse the leaf nodes in the right subtree [left -> right]
4. Traverse the nodes in the right boundary [bottom -> up]

## Code Dissection - exterior_binary_tree
1. Check for an empty tree
    ```python
    if not tree:
        return []
    ```
2. Create a list to hold the traversal with the root as its first element
    ```python
    exterior = [tree]
    ```
3. Traverse the nodes in the left boundary [top -> down]
    ```python
    left_boundary(tree.left)
    ```
4. Traverse the leaf nodes in the left subtree [left -> right]
    ```python
    leaves(tree.left)
    ```
5. Traverse the leaf nodes in the right subtree [left -> right]
    ```python
    leaves(tree.right)
    ```
6. Traverse the nodes in the right boundary [bottom -> up]
    ```python
    right_boundary(tree.right)
    ```
7. Return the exterior traversal
    ```python
    return exterior
    ```

## Code Dissection - left_boundary
1. Check for null and skip leaf nodes
    ```python
    if not tree or (not tree.left and not tree.right):
        return
    ```
2. Append the current node to the exterior list
    ```python
    exterior.append(tree)
    ```
3. Traverse left if the left subtree is not empty, otherwise, go right
    ```python
    if tree.left:
        left_boundary(tree.left)
    else:
        left_boundary(tree.right)
    ```

## Code Dissection - right_boundary
1. Check for null and skip leaf nodes
    ```python
    if not tree or (not tree.left and not tree.right):
        return
    ```
2. Traverse right if the right subtree is not empty, otherwise, go left
    ```python
    if tree.left:
        left_boundary(tree.left)
    else:
        left_boundary(tree.right)
    ```
3. Append the current node to the exterior list
    ```python
    exterior.append(tree)
    ```

## Code Dissection - leaves
1. Check for null
    ```python
    if not tree:
        return
    ```
2. If the node is a leaf node, append it to the exterior list, then return to prevent unnecessary recursive calls
    ```python
    if not tree.left and not tree.right:
        exterior.append(tree)
        return
    ```
3. Process the left and right subtree
    ```python
    leaves(tree.left)
    leaves(tree.right)
    ```