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
                          = 22 (base 10)
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
* BLANK

## Code Dissection
1. BLANK