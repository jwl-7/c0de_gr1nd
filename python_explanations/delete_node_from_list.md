# Delete a Node from a Singly Linked List
Write a program which deletes a node in a singly linked list. The input node is guaranteed not to be the tail node.

## Example
```
node_to_delete = 2

 Input: L -> [1] -> [2] -> [3] -> [4] -> [5] -> None
Output: L -> [1] -> [3] -> [4] -> [5] -> None
```

## Solution
```python
def deletion_from_list(node_to_delete):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next
```

## Explanation
* The data in the next node is copied into the node to delete, then the next node is deleted, which effectively deletes the current node

## Code Dissection
1. Copy the data from the next node into the current node
    ```python
    node_to_delete.data = node_to_delete.next.data
    ```
2. Set the current node to point to the next-next node
    ```python
    node_to_delete.next = node_to_delete.next.next
    ```