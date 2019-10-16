# Compute Binary Tree Nodes in Order of Increasing Depth
Given a binary tree, return an array consisting of the keys at the same level. keys should appear in the order of the corresponding nodes' depths, breaking ties from left to right.

## Example
```
    3
   / \
  9  20
    /  \
   15   7

 Input: [3, 9, 20, null, null, 15, 7]
Output: [
        [3],
        [9, 20],
        [15, 7]
    ]
```

## Solution
```python
def binary_tree_depth_order(tree):
    result = []
    level = [tree]
    while tree and level:
        curr_nodes = []
        next_level = []
        for node in level:
            curr_nodes.append(node.data)
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        result.append(curr_nodes)
        level = next_level
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK