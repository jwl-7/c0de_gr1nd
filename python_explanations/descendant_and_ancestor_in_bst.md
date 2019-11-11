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
1. Set an _a_ to _node0_ and _b_ to _node1_
2. Move _a_ and _b_ down the tree until:
    1. _a_ or _b_ is the _middle_ node
    2. _a_ is _b_ or _b_ is _a_
    3. We get to the bottom of the tree without reaching the first two cases
3. Check the results from the search:
    1. If _a_ or _b_ is _middle_, then _a_ or _b_ is an ancestor of _middle_
    2. If _a_ is _b_ or _b_ is _a_, then the _middle_ can't be between _a_ and _b_
4. If _a_ or _b_ is an ancestor of middle, then check if _middle_ is an ancestor of _node0_ or _node1_ by moving down the tree
5. If _middle_ is an ancestor of _node0_ or _node1_ at this point, then the 3 nodes are ordered

## Code Dissection - pair_includes_ancestor_and_descendant_of_m
1. Set two variables _a_ and _b_ to _node0_ and _node1_ respectively
    ```python
    a = node0
    b = node1
    ```
2. Move _a_ and _b_ down the tree to check if _node0_ or _node1_ is an ancestor of _middle_
    ```python
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
    ```
    1. _a_ or _b_ is the _middle_ node
    2. _a_ is _b_ or _b_ is _a_
    3. We get to the bottom of the tree without reaching the first two cases
3. Check the results from the previous search
    ```python
    if (
        a is not middle and
        b is not middle or
        a is node1 or
        b is node0
    ):
        return False
    ```
    1. If _a_ or _b_ is _middle_, then _a_ or _b_ is an ancestor of _middle_
    2. If _a_ is _b_ or _b_ is _a_, then the _middle_ can't be between _a_ and _b_
4. If _a_ or _b_ is an ancestor of middle, then check if _middle_ is an ancestor of _node0_ or _node1_
    ```python
    return search_bst(middle, node1 if a is middle else node0)
    ```
    * If _middle_ is an ancestor of _node0_ or _node1_, then the nodes are ordered, and this statement will return True

## Code Dissection - search_bst
1. Move the source node down the tree until we hit the target node or the bottom of the tree
    ```python
    while tree and tree is not node:
        tree = tree.left if tree.data > node.data else tree.right
    ```
2. If we find the target node from the source node, then return True
    ```python
    return tree is node
    ```