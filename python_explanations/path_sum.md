# Find a Root to Leaf Path with Specified Sum
Given a binary tree and an integer, determine if the tree contains a root-to-leaf path such that the numbers add up to the given sum.

## Examples
```
        1
       / \
      2   3
     / \
    7   5

 Input: [1, 2, 3, 7, 5, null, null]
        weight = 10
Output: True


 Input: [1, 2, 3, 7, 5, null, null]
        weight = 4
Output: True


 Input: [1, 2, 3, 7, 5, null, null]
        weight = 9
Output: False
```

## Solution
```python
def has_path_sum(tree, remaining_weight):
    if not tree:
        return False
    if not tree.left and not tree.right:
        return remaining_weight == tree.data
    return (
        has_path_sum(tree.left, remaining_weight - tree.data) or
        has_path_sum(tree.right, remaining_weight - tree.data)
    )
```

## Explanation
* The solution traverses each root-to-leaf path, subtracting each node's weight in the path from the given weight, and checking if the remaining weight is equal to the leaf's weight

## Code Dissection
1. Check if the tree is empty
    ```python
    if not tree:
        return False
    ```
2. If the node is a leaf, check if the remaining weight is the same as the leaf's weight
    ```python
    if not tree.left and not tree.right:
        return remaining_weight == tree.data
    ```
3. If the node is not a leaf, keep processing the root-to-leaf path and subtracting from the remaining weight
    ```python
    return (
        has_path_sum(tree.left, remaining_weight - tree.data) or
        has_path_sum(tree.right, remaining_weight - tree.data)
    )
    ```