# Generate Binary Trees
Given an integer _n_, return all distinct binary trees with _n_ nodes.

## Example
```
 Input: 3
Output:

      O     O        O    O            O
     / \     \      /      \          /
    O   O     O    O        O        O
             /      \        \      /
            O        O        O    O
```

## Solution
```python
def generate_all_binary_trees(num_nodes):
    if not num_nodes:
        return [None]

    result = []
    for num_left in range(num_nodes):
        num_right = num_nodes - 1 - num_left
        left_tree = generate_all_binary_trees(num_left)
        right_tree = generate_all_binary_trees(num_right)
        result += [
            BinaryTreeNode(0, left, right)
            for left in left_tree
            for right in right_tree
        ]
    return result
```

## Explanation
* To generate all binary trees with _n_ nodes, generate all left subtrees with _i_ nodes and right subtrees with _n_ - 1 - _i_ nodes for _i_ in the range [0, _n_-1]

## Code Dissection
1. If the number of nodes is zero, then return an empty tree
    ```python
    if not num_nodes:
        return [None]
    ```
2. Create a list to store all the trees
    ```python
    result = []
    ```
3. For _n_ nodes, generate the left subtrees with _i_ nodes and right subtrees with _n_ - 1 - _i_ nodes
    ```python
    num_right = num_nodes - 1 - num_left
    left_tree = generate_all_binary_trees(num_left)
    right_tree = generate_all_binary_trees(num_right)
    ```
4. Generate the combinations for the left and right subtrees, then add the tree to the result
    ```python
    result += [
        BinaryTreeNode(0, left, right)
        for left in left_tree
        for right in right_tree
    ]
    ```
5. Return all the distinct binary trees
    ```python
    return result
    ```