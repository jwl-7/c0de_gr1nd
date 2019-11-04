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
1. Create a simple hash table to store the visited nodes
    ```python
    ancestors = set()
    ```
2. Loop while either node exists and the LCA hasn't been found
    ```python
    while node0 or node1:
    ```
3. For _node0_, traverse up the tree, add the visited node to the hash table &mdash; if the node is already in the table, then it's the LCA
    ```python
    if node0:
        if node0 in ancestors:
            return node0
        ancestors.add(node0)
        node0 = node0.parent
    ```
4. For _node1_, traverse up the tree, add the visited node to the hash table &mdash; if the node is already in the table, then it's the LCA
    ```python
    if node1:
        if node1 in ancestors:
            return node1
        ancestors.add(node1)
        node1 = node1.parent
    ```