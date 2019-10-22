# Implement an Inorder Traversal Without Recursion
Write a program which takes as input a binary tree and performs an inorder traversal of the tree. Do not use recursion. Nodes do not contain parent references.

## Example
```
        1
       / \
      2   3
     / \
    7   5

 Input: [1, 2, 3, 7, 5, null, null]
Output: [7, 2, 5, 1, 3]
```

## Solution
```python
def inorder_traversal(tree):
    stack = []
    result = []
    while stack or tree:
        if tree:
            stack.append(tree)
            tree = tree.left
        else:
            tree = stack.pop()
            result.append(tree.data)
            tree = tree.right
    return result
```

## Explanation
* The solution uses a stack to traverse the tree without recursion

The algorithm is as follows:
1. Create an empty stack
2. While the current node is not null:
    1. Push the current node to the stack
    2. Go left
3. Else if the current node is null:
    1. Set the current node to the top of the stack (go up)
    2. Push the current node to the result list
    3. Go right
4. If the current node is null and the stack is empty, then the traversal is done

## Code Dissection
1. Create an empty stack and a list to hold the traversal
    ```python
    stack = []
    result = []
    ```
2. Loop while the _stack_ isn't empty or the current node is not null
    ```python
    while stack or tree:
    ```
3. If the current node is not null, push it to the stack and go left
    ```python
    if tree:
        stack.append(tree)
        tree = tree.left
    ```
4. If the current node is null, set the current node to the top of the _stack_ to go up, push the new current node to the _result_ list, and then go right
    ```python
    else:
        tree = stack.pop()
        result.append(tree.data)
        tree = tree.right
    ```
5. Return the inorder traversal
    ```python
    return result
    ```