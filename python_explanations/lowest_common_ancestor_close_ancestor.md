# Compute the LCA, Optimizing for Close Ancestors
Given 2 nodes in a binary tree, compute the LCA.

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
def lca(node0, node1):
    ancestors = set()
    while node0 or node1:
        if node0:
            if node0 in ancestors:
                return node0
            ancestors.add(node0)
            node0 = node0.parent
        if node1:
            if node1 in ancestors:
                return node1
            ancestors.add(node1)
            node1 = node1.parent
```

## Explanation
* Traverse up the tree from each node simultaneously while storing the visited nodes in a hash table
* If one of the current nodes is already in the hash table, then its the LCA

## Code Dissection
1. BLANK