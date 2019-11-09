# Reconstruct a BST from Traversal Data
Given a preorder sequence, reconstruct the BST.

## Example
```
 Input: preorder = [4, 2, 1, 3, 5]
Output:

        4
       / \
      2   5
     / \
    1   3
```

## Solution
```python
def rebuild_bst_from_preorder(preorder_sequence):
    if not preorder_sequence:
        return None

    root = BinaryTreeNode(preorder_sequence[0])
    i = 1
    while i < len(preorder_sequence):
        if preorder_sequence[i] < preorder_sequence[0]:
            i += 1
        else:
            break

    root.left = rebuild_bst_from_preorder(preorder_sequence[1:i])
    root.right = rebuild_bst_from_preorder(preorder_sequence[i:])
    return root
```

## Explanation
* Since this is a BST, we can identify which nodes lie in the left and right subtree respectively since the root is the first node in the preorder sequence
* Making use of the recursive call stack, the solution identifies and connects the nodes based on the range of numbers less than or greater than the root

## Code Dissection
1. Base case: stop recursing when we reach the end of a range (numbers in the preorder sequence to process)
    ```python
    if not preorder_sequence:
        return None
    ```
2. Set the root as the first number in the sequence
    ```python
    root = TreeNode(preorder_sequence[0])
    ```
3. Compute the range of numbers that belong in the left subtree and right tree respectively
    ```python
    i = 1
    while i < len(preorder_sequence):
        if preorder_sequence[i] < preorder_sequence[0]:
            i += 1
        else:
            break
    ```
    * `preorder_sequence[1:i]` = nodes < root = left subtree
    * `preorder_sequence[i:]` = nodes > root = right subtree
4. Build the left and right subtrees
    ```python
    root.left = rebuild_bst_from_preorder(preorder_sequence[1:i])
    root.right = rebuild_bst_from_preorder(preorder_sequence[i:])
    ```
5. Return the root of the BST after building the tree
    ```python
    return root
    ```