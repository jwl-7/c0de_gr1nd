# Implement List Pivoting
For any integer _k_, the pivot of a list of integers with respect to _k_ is that list with its nodes reordered so that all nodes containing keys less than _k_ appear before nodes containing _k_, and all nodes containing keys greater than _k_ appear after the nodes containing _k_.  
  
Implement a function which takes as input a singly linked list and an integer _k_ and performs a pivot of the list with respect to _k_. The relative ordering of nodes that appear before _k_, and after _k_, must remain unchanged; the same must hold for nodes holding keys equal to _k_.
  
## Example
```
x = 7

 Input: L -> [3] -> [2] -> [2] -> [11] -> [7] -> [5] -> [11] -> None
Output: L -> [3] -> [2] -> [2] -> [5] -> [7] -> [11] -> [11] -> None
```
  
## Solution
```python
def list_pivoting(L, x):
    less_head = less = ListNode()
    equal_head = equal = ListNode()
    greater_head = greater = ListNode()
    while L:
        if L.data < x:
            less.next = L
            less = less.next
        elif L.data == x:
            equal.next = L
            equal = equal.next
        elif L.data > x:
            greater.next = L
            greater = greater.next
        L = L.next
    greater.next = None
    equal.next = greater_head.next
    less.next = equal_head.next
    return less_head.next
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK