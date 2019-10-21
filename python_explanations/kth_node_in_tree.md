# Compute the *k*th Node in an Inorder Traversal
Write a program that efficiently computes the *k*th node appearing in an inorder traversal. Assume that each node stores the number of nodes in the subtree rooted at that node.

## Example
```
       1
      / \
     2   3
    / \
   7   5

Inorder Traversal: [7, 2, 5, 1, 3]

 Input: [1, 2, 3, 7, 5, null, null]
        k = 3
Output: 5
```

## Solution
```python
def find_kth_node_binary_tree(tree, k):
    while tree:
        left_size = tree.left.size if tree.left else 0
        if left_size + 1 < k:
            k -= left_size + 1
            tree = tree.right
        elif left_size == k - 1:
            return tree
        else:
            tree = tree.left
    return None
```

## Explanation
* BLANK

## Code Dissection
1. BLANK