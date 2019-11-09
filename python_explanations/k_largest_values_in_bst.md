# Find the _k_ Largest Elements in a BST
BLANK

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
* BLANK

## Code Dissection
1. BLANK