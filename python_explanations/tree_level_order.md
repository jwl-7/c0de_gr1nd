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
        result.append([node.data for node in level])
        next_level = []
        for node in level:
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)
        level = next_level
    return result
```

## Explanation
* The solution implements a [Breadth-First Traversal](https://en.wikipedia.org/wiki/Breadth-first_search) (BFS), also referred to as a Level Order Traversal
* Starting at the tree root, for each node, the first node is visited and its child nodes are put in a FIFO queue
* To put it another way, the solution iterates over each node in the binary tree from left to right level by level, and appends each level as a list in the result list

## Code Dissection
1. Create an empty list to hold the BFS traversal and the level (which starts at the root of tree)
    ```python
    result = []
    level = [tree]
    ```
2. Loop while _tree_ and _level_ contain data