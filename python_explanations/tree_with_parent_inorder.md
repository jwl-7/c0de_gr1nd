# Implement an Inorder Traversal with _O(1)_ Space
Given a binary tree, return the inorder traversal. The nodes contain parent pointers, and the solution must be iterative.

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
* For an explanation on computing the next node in an inorder traversal: [Compute the Successor](successor_in_tree.md)
* The solution iterates to the leftmost node, the first node in the traversal, then keeps finding the successor to the current node until reaching the rightmost element

## Code Dissection
1. Create an empty list to store the inorder traversal
    ```python
    result = []
    ```
2. Find the leftmost node in the tree, which is the first node in the traversal
    ```python
    while tree and tree.left:
        tree = tree.left
    ```
3. Keep computing the successor to the current node and appending the current node's data to _result_ until reaching the rightmost node
    ```python
    while tree:
        result.append(tree.data)
    ```
4. If the right subtree exists, find the leftmost node in the right subtree
    ```python
    if tree.right:
        tree = tree.right
        while tree.left:
            tree = tree.left
    ```
5. If the right subtree does not exist, find the parent whose left subtree contains the current node
    ```python
    else:
        while tree.parent and tree.parent.right is tree:
            tree = tree.parent
        tree = tree.parent
    ```
6. Return the inorder traversal
    ```python
    return result
    ```