# Delete a Node from a Singly Linked List
Write a program which deletes a node in a singly linked list. The input node is guaranteed not to be the tail node.
  
## Example
```
 Input: [L] -> [1] -> [2] -> [3] -> [4] -> [5] -> None
        node_to_delete = 2
Output: [L] -> [1] -> [3] -> [4] -> [5] -> None
```
  
## Solution
```python
def deletion_from_list(node_to_delete):
    node_to_delete.data = node_to_delete.next.data
    node_to_delete.next = node_to_delete.next.next
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK