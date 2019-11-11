# Test If Three BST Nodes Are Totally Ordered
Given two nodes in a BST, check if one is an ancestor and the other a descendant of the given middle node.

## Examples
```
        4
       / \
      2   5
     / \
    1   3

 Input:  node0 = 1
         node1 = 4
        middle = 2
Output: True
Conclusion: 4 is an ancestor of 2
            1 is a descendant of 2


 Input:  node0 = 1
         node1 = 3
        middle = 2
Output: False
Conclusion: 1 and 3 are descendants of 2
```

## Solution
```python
def pair_includes_ancestor_and_descendant_of_m(node0, node1, middle):
    a = node0
    b = node1
    while (
        a is not node1 and
        a is not middle and
        b is not node0 and
        b is not middle and
        (a or b)
    ):
        if a:
            a = a.left if a.data > middle.data else a.right
        if b:
            b = b.left if b.data > middle.data else b.right

    if (
        a is not middle and
        b is not middle or
        a is node1 or
        b is node0
    ):
        return False

    return search_bst(middle, node1 if a is middle else node0)


def search_bst(tree, node):
    while tree and tree is not node:
        tree = tree.left if tree.data > node.data else tree.right
    return tree is node
```

## Explanation
* BLANK

## Code Dissection
1. BLANK