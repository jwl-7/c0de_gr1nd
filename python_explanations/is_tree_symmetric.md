# Test If a Binary Tree Is Symmetric
A binary tree is symmetric if you can draw a vertical line through the root and then the left subtree is the mirror image of the right subtree.

Write a program that checks whether a binary tree is symmetric.

## Examples
```
    1
   / \
  2   2
 / \ / \
3  4 4  3

 Input: [1, 2, 2, 3, 4, 4, 3]
Output: True


    1
   / \
  2   2
   \   \
   3    3

 Input: [1, 2, 2, null, 3, null, 3]
Output: False
```

## Solution
```python
def is_mirror(L, R):
    if not L and not R:
        return True
    elif L and R and L.data == R.data:
        return is_mirror(L.right, R.left) and is_mirror(L.left, R.right)
    return False


def is_symmetric(tree):
    return is_mirror(tree, tree)
```

## Explanation
Two trees are a mirror reflection of each other if:
1. Their two roots have the same value
2. The left subtree of the left tree and the right subtree of the right tree are mirror images
3. The right subtree of the left tree and the left subtree of the right tree are mirror images

## Code Dissection - is_mirror
1. If the left and right subtree are empty, then they are mirror images
    ```python
    if not L and not R:
        return True
    ```
    * This will also perform the initial check for an empty tree
2. If the left and right subtree are not empty and the two subtree root nodes have the same data, then check the left subtree and right subtree
    ```python
    elif L and R and L.data == R.data:
        return is_mirror(L.right, R.left) and is_mirror(L.left, R.right)
    ```
3. If the two subtree root nodes do not have the same data, then they are not mirror images
    ```python
    return False
    ```

## Code Dissection - is_symmetric
1. Return whether or not the _tree_ is symmetric
    ```python
    return is_mirror(tree, tree)
    ```