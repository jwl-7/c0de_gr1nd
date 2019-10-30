# Compute the Right Sibling Tree
For this problem, assume that each binary tree node has an extra field, call it level-next, that holds a binary tree node (this field is distinct from the fields for the left and right children). The level-next field will be used to compute a map from nodes to their right siblings. The input is assumed to be a perfect binary tree.

Write a program that takes a perfect binary tree, and sets each node's level-next field to the node on its right, if one exists.

## Example
```
Input:            Output:
        11                 11-->None
       /  \               /  \
      2    3             2--->3-->None
     / \  / \           / \  / \
    4  5  6  7         4->5->6->7-->None
```

## Solution
```python
def construct_right_sibling(tree):
    while tree:
        curr = tree
        while curr and curr.left:
            curr.left.next = curr.right
            if curr.next:
                curr.right.next = curr.next.left
            curr = curr.next
        tree = tree.left
```

## Explanation
* The solution traverses the tree level-by-level from [left -> right]
* For each level, the next fields for the nodes on the level below are processed

## Code Dissection
1. Start traversing from the root of the tree using a pointer that will represent the starting node for each level
    ```python
    while tree:
        curr = tree
    ```
2. Loop until we are done processing the nodes for the current level
    ```python
    while curr and curr.left:
    ```
3. On the level below the current node, connect the left node to the right node
    ```python
    curr.left.next = curr.right
    ```
4. If the current node's next field isn't null, on the level below, connect the right node to the left node in the subtree beside it
    ```python
    if curr.next:
        curr.right.next = curr.next.left
    ```
5. Set the current node to the node we just connected it to
    ```python
    curr = curr.next
    ```
    * If _curr_ = None, then that means we are done processing the current level
6. Go to the next level below starting on the left
    ```python
    tree = tree.left
    ```