# Remove the *k*th Last Element from a List
Given a singly linked list and an integer _k_, write a program to remove the *k*th last element from the list. Your algorithm cannot use more than a few words of storage, regardless of the length of the list. In particular, you cannot assume that it is possible to record the length of the list.
  
## Example
```
BLANK
```
  
## Solution
```python
def remove_kth_last(L, k):
    slow = fast = L
    for _ in range(k):
        fast = fast.next
    if not fast:
        return L.next
    while fast.next:
        fast = fast.next
        slow = slow.next
    slow.next = slow.next.next
    return L
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK