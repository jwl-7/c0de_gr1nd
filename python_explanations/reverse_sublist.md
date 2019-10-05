# Reverse a Single Sublist
This problem is concerned with reversing a sublist within a list.  
  
Write a program which takes a singly linked list _L_ and two integers _s_ and _f_ as arguments, and reverses the order of the nodes from the *s*th node to *f*th node, inclusive. The numbering begins at 1, i.e., the head node is the first node. Do not allocate additional nodes.
  
## Example
```
s = 2
f = 4

 Input: [L] -> [1] -> [2] -> [3] -> [4] -> [5] -> None
Output: [L] -> [1] -> [4] -> [3] -> [2] -> [7] -> None
```
  
## Solution
```python
def reverse_sublist(L, start, finish):
    dummy = subhead = ListNode()
    dummy.next = L

    for _ in range(1, start):
        subhead = subhead.next
    subtail = subhead.next

    for _ in range(start, finish):
        tmp = subhead.next
        subhead.next = subtail.next
        subtail.next = subtail.next.next
        subhead.next.next = tmp
    return dummy.next
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK
  
## Step-by-Step Example
<img src='drawio_diagrams/reverse_sublist.svg' width='100%'>