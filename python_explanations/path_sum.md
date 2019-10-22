# Find a Root to Leaf Path with Specified Sum
You are given a binary tree where each node is labeled with an integer. The path weight of a node in such a tree is the sum of the integers on the unique path from the root to that node.

Write a program which takes as input an integer and a binary tree with integer node weights, and checks if there exists a leaf whose path weight equals the given integer.

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