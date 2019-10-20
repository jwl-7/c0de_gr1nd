# Compute the LCA When Nodes Have Parent Pointers
Given two nodes in a binary tree, design an algorithm that computes their LCA. Assume that each node has a parent pointer.

## Examples
```
    3
   / \
  5   1
 / \ / \
6  2 0  8
  / \
 7   4

 Input: node0 = 5
        node1 = 1
Output: 3

 Input: node0 = 5
        node1 = 4
Output: 5
```

## Solution
```python
def depth(node):
    depth = 0
    while node:
        node = node.parent
        depth += 1
    return depth


def lca(node0, node1):
    depth0 = depth(node0)
    depth1 = depth(node1)
    if depth1 > depth0:
        node0, node1 = node1, node0

    diff = abs(depth0 - depth1)
    while diff:
        node0 = node0.parent
        diff -= 1

    while node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent
    return node0
```

## Explanation
1. Find the depth of each node by ascending up towards the root using the parent pointers
2. Ascend from the lower node (higher depth) to the depth of the higher node (lower depth)
3. Ascend from both nodes towards the root while checking for the LCA

## Code Dissection - depth
1. Create an integer variable to hold the depth of the node
    ```python
    depth = 0
    ```
2. Ascend towards the root of the tree using the parent pointers and increment the _depth_
    ```python
    while node:
        node = node.parent
        depth += 1
    ```
3. Return the _depth_ of the _node_
    ```python
    return depth
    ```

## Code Dissection - lca
1. Find the depth of both nodes
    ```python
    depth0 = depth(node0)
    depth1 = depth(node1)
    ```
2. Make sure _node0_ is the deeper node, which helps simplify the algorithm
    ```python
    if depth1 > depth0:
        node0, node1 = node1, node0
    ```
3. Find the difference between the two depths
    ```python
    diff = abs(depth0 - depth1)
    ```
4. Ascend from the lower node to the depth of the higher node
    ```python
    while diff:
        node0 = node0.parent
        diff -= 1
    ```
5. Ascend from both nodes until reaching the LCA
    ```python
    while node0 is not node1:
        node0 = node0.parent
        node1 = node1.parent
    ```
6. Return the LCA
    ```python
    return node0
    ```