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
* BLANK

## Code Dissection - depth
1. BLANK

## Code Dissection - lca
1. BLANK