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
        num_right = num_nodes - num_left - 1
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
* BLANK

## Code Dissection
1. BLANK