# Sum the Root-To-Leaf Paths in a Binary Tree
Consider a binary tree in which each node contains a binary digit. A root-to-leaf path can be associated with a binary number&mdash;the MSB is at the root.

Design an algorithm to compute the sum of the binary numbers represented by the root-to-leaf paths.

## Examples
```
        1
       / \
      0   1
     / \ / \
    0  1 1  0

 Input: [1, 0, 1, 0, 1, 1, 0]
Output: 22

The binary numbers represented by this tree are:
    100 + 101 + 111 + 110 = 10110 (base 2)
     4  +  5  +  7  +  6  =    22 (base 10)
```

## Solution
```python
def sum_root_to_leaf(tree, partial_path_sum=0):
    if not tree:
        return 0

    partial_path_sum = partial_path_sum * 2 + tree.data
    if not tree.left and not tree.right:
        return partial_path_sum

    return (
        sum_root_to_leaf(tree.left, partial_path_sum) +
        sum_root_to_leaf(tree.right, partial_path_sum)
    )
```

## Explanation
* The solution performs a preorder DFS to calculate the sum of all the root-to-leaf paths
* If the node is a leaf we return its integer
* If the node is not a leaf, we return the sum of the results from its left and right children

## Code Dissection
1. Check if the tree is empty
    ```python
    if not tree:
        return 0
    ```
2. Keep track of the partial sum in an integer format
    ```python
    partial_path_sum = partial_path_sum * 2 + tree.data
    ```
3. If the node is a leaf, return the partial sum
    ```python
    if not tree.left and not tree.right:
        return partial_path_sum
    ```
4. If the node is not a leaf, return the sum of the results from its left and right children
    ```python
    return (
        sum_root_to_leaf(tree.left, partial_path_sum) +
        sum_root_to_leaf(tree.right, partial_path_sum)
    )
    ```