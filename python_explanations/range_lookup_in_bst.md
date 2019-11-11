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
* BLANK

## Code Dissection
1. BLANK