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
        if k == left_size + 1:
            return tree
        elif k > left_size:
            tree = tree.right
            k -= left_size + 1
        else:
            tree = tree.left
    return None
```

## Explanation
Let _L_ be the number of nodes in the left subtree:
    * If _k_ > _L_, then the *k*th node lies in the right subtree
    * If _k_ <= _L_, then the *k*th node lies in the left subtree
    * The *k*th node in the original tree is the (_k_ - _L_)th node when skipping the left subtree
* If the left subtree has _L_ nodes, then the *k*th node in the original tree is the (_k_ - _L_)th node

Now that we understand where the *k*th node is, the algorithm for the solution is as follows:
* Skip the left or right subtree depending on the number of nodes in that subtree
* When skipping the left subtree, subtract _L_ + 1 from _k_

## Code Dissection
1. Loop while the (sub)tree is not null
    ```python
    while tree:
    ```
2. Set a variable to store the size (number of nodes) in the left subtree
    ```python
    left_size = tree.left.size if tree.left else 0
    ```
3. If _k_ = *left_size* + 1, then the current node is the *k*th node
    ```python
    if k == left_size + 1:
        return tree
    ```
4. If _k_ > *left_size*, then the *k*th node is in the right subtree
    ```python
    elif k > left_size:
        tree = tree.right
        k -= left_size + 1
    ```
5. If _k_ <= *left_size*, then the *k*th node is in the left subtree
    ```python
    else:
        tree = tree.left
    ```