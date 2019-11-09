# Find the _k_ Largest Elements in a BST
Given a BST and an integer _k_, return the _k_ largest elements in descending order.

## Example
```
        4
       / \
      2   5
     / \
    1   3

 Input: k = 2
Output: [4, 5]
```

## Solution
```python
def find_k_largest_in_bst(tree, k):
    def helper(tree):
        if tree and len(result) < k:
            helper(tree.right)
            if len(result) < k:
                result.append(tree.data)
                helper(tree.left)

    result = []
    helper(tree)
    return result
```

## Explanation
* The solution performs a reverse inorder traversal

## Code Dissection - helper
1. Recurse the right subtree
    ```python
    if tree and len(result) < k:
        helper(tree.right)
    ```
2. Add the value to the result, if we are still searching for elements
    ```python
    if len(result) < k:
        result.append(tree.data)
    ```
3. Recurse the left subtree, which results in a reverse inorder traversal
    ```python
    helper(tree.left)
    ```

## Code Dissection - find_k_largest_in_bst
1. Create an array to hold the _k_ largest elements
    ```python
    result = []
    ```
2. Call the recursive `helper()` function to perform a reverse inorder traversal
    ```python
    helper(tree)
    ```
3. Return the _k_ largest elements
    ```python
    return result
    ```