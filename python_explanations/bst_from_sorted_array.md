# Build a Minimum Height BST from a Sorted Array
Given a sorted array, build a BST with the smallest possible height.

## Example
```
 Input: [1, 2, 3, 4, 5, 6, 7]
Output:
        4
       / \
      2   6
     / \ / \
    1  3 5  7

 Height = 2
```

## Solution
```python
def build_min_height_bst_from_sorted_array(A):
    if not A:
        return None
    mid = len(A) // 2
    root = BinaryTreeNode(A[mid])
    root.left = build_min_height_bst_from_sorted_array(A[:mid])
    root.right = build_min_height_bst_from_sorted_array(A[mid+1:])
    return root
```

## Explanation
* Given that the array is sorted&mdash;for a minimum height tree, the root will be the middle element in the array

## Code Dissection
1. Base case: if _A_ is empty, then return
    ```python
    if not A:
        return None
    ```
2. Compute the middle index in _A_, then add the middle element as the root
    ```python
    mid = len(A) // 2
    root = BinaryTreeNode(A[mid])
    ```
3. Build the left and right subtrees
    ```python
    root.left = build_min_height_bst_from_sorted_array(A[:mid])
    root.right = build_min_height_bst_from_sorted_array(A[mid+1:])
    ```
4. Return the root of the BST
    ```python
    return root
    ```