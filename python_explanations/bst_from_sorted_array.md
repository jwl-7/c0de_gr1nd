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
* BLANK

## Code Dissection
1. BLANK