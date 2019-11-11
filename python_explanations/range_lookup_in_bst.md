# The Range Lookup Problem
Given a BST and an interval, return the node keys within the interval.

## Example
```
        4
       / \
      2   6
     / \ / \
    1  3 5  7

 Input: interval = [1, 4]
Output: [1, 2, 3, 4]
```

## Solution
```python
Interval = collections.namedtuple('Interval', ('left', 'right'))


def range_lookup_in_bst(tree, interval):
    def helper(tree):
        if tree:
            if interval.left < tree.data:
                helper(tree.left)
            if interval.left <= tree.data <= interval.right:
                result.append(tree.data)
            if interval.right > tree.data:
                helper(tree.right)

    result = []
    helper(tree)
    return result
```

## Explanation
* If the current node < left interval, then search the right subtree
* If the current node > right interval, then search the left subtree

## Code Dissection - helper
1. Base case: if _tree_ is empty, then return
    ```python
    if tree:
    ```
2. If current node > left interval, go left
    ```python
    if interval.left < tree.data:
        helper(tree.left)
    ```
3. If current node is within the interval, add its key to the result
    ```python
    if interval.left <= tree.data <= interval.right:
        result.append(tree.data)
    ```
4. If current node < right interval, go right
    ```python
    if interval.right > tree.data:
        helper(tree.right)
    ```

## Code Dissection - range_lookup_in_bst
1. Create a list to store the result, call `helper()`, then return the result
    ```python
    result = []
    helper(tree)
    return result
    ```