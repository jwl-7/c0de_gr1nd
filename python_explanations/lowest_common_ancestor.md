# Compute the Lowest Common Ancestor in a Binary Tree
Any two nodes in a binary tree have a common ancestor, namely the root. The lowest common ancestor (LCA) of any two nodes in a binary tree is the node furthest from the root that is an ancestor of both nodes.

Design an algorithm for computing the LCA of two nodes in a binary tree in which nodes do not have a parent field.

## Examples
```
        3
       / \
      5   1
     / \ / \
    6  2 0  8
       / \
      7   4

 Input: [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
        node0 = 5
        node1 = 1
Output: 3


 Input: [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]
        node0 = 5
        node1 = 4
Output: 5
```

## Solution
```python
def lca(tree, node0, node1):
    if not tree or tree == node0 or tree == node1:
        return tree
    left = lca(tree.left, node0, node1)
    right = lca(tree.right, node0, node1)
    return tree if left and right else left or right
```

## Explanation
1. Start traversing the tree from the root
2. If any of the given keys (node0 and node1) matches with the root, then the root is the LCA
3. If the root doesn't match with any of the keys, we recur for the left and right subtree
4. The node which has one key present in its left subtree and the other key present in its right subtree is the LCA
5. If both keys lie in the in the left subtree or the right subtree, then the LCA is the root of that subtree


## Code Dissection
1. If the (sub)tree is empty or it matches with any of the given keys, then return the root
    ```python
    if not tree or tree == node0 or tree == node1:
        return tree
    ```
2. Search the left and right subtree
    ```python
    left = lca(tree.left, node0, node1)
    right = lca(tree.right, node0, node1)
    ```
3. For the return statement, there are 3 cases:
    1. If the current subtree contains both node0 and node1, then return that subtree as the LCA
    2. If only one of the keys is in the subtree, then return that key
    3. If neither of the keys are in the subtree, then return `None`
    ```python
    return tree if left and right else left or right
    ```