# Implement Cyclic Right Shift for Singly Linked Lists
Write a program that takes as input a singly linked list and a nonnegative integer _k_, and returns the list cyclically shifted to the right by _k_.
  
## Example
```
k = 3

 Input: L -> [1] -> [2] -> [3] -> [4] -> [5] -> None
Output: L -> [3] -> [4] -> [5] -> [1] -> [2] -> None
```
  
## Solution
```python
def cyclically_right_shift_list(L, k):
    if not L:
        return None

    tail = L
    n = 1
    while tail.next:
        tail = tail.next
        n += 1

    k %= n
    if k == 0:
        return L

    tail.next = L
    for _ in range(n - k):
        tail = tail.next
        
    L = tail.next
    tail.next = None
    return L
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK