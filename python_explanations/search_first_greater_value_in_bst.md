# Find the First Key Greater Than a Given Value in a BST
Given a BST and a value _k_, return the first node in an inorder traversal greater than _k_.

## Example
```
        4
       / \
      2   5
     / \
    1   3

Inorder Traversal: [1, 2, 3, 4, 5]

 Input: k = 3
Output: 4
```

## Solution
```python
def find_first_greater_than_k(tree, k):
    result = None
    while tree:
        if tree.data > k:
            result = tree
            tree = tree.left
        else:
            tree = tree.right
    return result
```

## Explanation
* Descend down the tree from the root and eliminate subtrees based on their root's value
* Update the result while traversing until reaching the bottom of the tree

## Code Dissection
1. Create an empty result variable&mdash;note that the problem wants the answer to be the node itself and not its value
    ```python
    result = None
    ```
2. Descend down the tree from the root until reaching the bottom
    ```python
    while tree:
    ```
3. If the node's key > _k_, update the result and keep going left
    ```python
    if tree.data > k:
        result = tree
        tree = tree.left
    ```
4. If the node's key <= _k_, skip the left subtree and go right
    ```python
    else:
        tree = tree.right
    ```
5. Return the final result after traversing
    ```python
    return result
    ```