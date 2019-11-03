# Compute Binary Tree Nodes in Order of Increasing Depth
Given a binary tree, return the level order traversal of its node keys.

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
1. Create an empty list to hold the level order traversal and a queue to hold to hold the nodes at each level (starts at the root of the tree)
    ```python
    result = []
    level = [tree]
    ```
2. Loop while _tree_ and _level_ contain data
    ```python
    while tree and level:
    ```
3. Append the nodes in the current level as a list in _result_
    ```python
    result.append([node.data for node in level])
    ```
4. Dequeue all the elements from *next_level*
    ```python
    next_level = []
    ```
5. For each node in the current level, enqueue its child nodes to *next_level*
    ```python
    for node in level:
        if node.left:
            next_level.append(node.left)
        if node.right:
            next_level.append(node.right)
    ```
6. After processing the current level, go to the next level
    ```python
    level = next_level
    ```
7. Return the level order traversal
    ```python
    return result
    ```