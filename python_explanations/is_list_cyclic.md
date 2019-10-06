# Test for Cyclicity
Although a linked list is supposed to be a sequence of nodes ending in null, it is possible to create a cycle in a linked list by making the next field of an element reference to one of the earlier nodes.  
  
Write a program that takes the head of a singly linked list and returns null if there does not exist a cycle, and the node at the start of the cycle, if a cycle is present. (You do not know the length of the list in advance.)
  
## Examples
<img src='drawio_diagrams/is_list_cyclic1.svg' width='75%'>

```
 Input: [1, 5, 7]
Output: None
```

<img src='drawio_diagrams/is_list_cyclic2.svg' width='75%'>

```
 Input: [1, 2, 3, 4]
Output: 2
```
  
## Solution
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            fast = head
            while fast is not slow:
                fast = fast.next
                slow = slow.next
            return fast
    return None
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK