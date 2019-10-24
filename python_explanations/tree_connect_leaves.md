# Form a Linked List from the Leaves of a Binary Tree
Given a binary tree, compute a linked list from the leaves of the binary tree. The leaves should appear in left-to-right order.

## Example
```
        1
       / \
      2   2
     / \ / \
    3  4 4  3

 Input: [1, 2, 2, 3, 4, 4, 3]
Output: [3, 4, 4, 3]
```

## Solution
```python
def create_list_of_leaves(tree):
    if not tree:
        return []
    elif not tree.left and not tree.right:
        return [tree]
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)
```

## Explanation
* Unfortunately the problem title and description are highly misleading as the book expects the output to be a regular Python list
* The solution processes the tree from left -> right and adds each leaf to the list
* The list object returned from the solution can easily be converted into a real linked list with an additional function that converts each list element into a node

## Code Dissection
1. If the _tree_ is empty, return an empty list
    ```python
    if not tree:
        return []
    ```
2. If the node is a leaf, add it to the list
    ```python
    elif not tree.left and not tree.right:
        return [tree]
    ```
3. Process the left subtree and the right subtree
    ```python
    return create_list_of_leaves(tree.left) + create_list_of_leaves(tree.right)
    ```