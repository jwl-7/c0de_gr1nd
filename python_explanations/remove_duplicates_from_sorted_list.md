# Remove Duplicates from a Sorted List
Write a program that takes as input a singly linked list of integers in sorted order, and removes duplicates from it. The list should be sorted.
  
## Example
```
 Input: L -> [1] -> [2] -> [2] -> [3] -> [5] -> [7] -> [11] -> [11] -> None
Output: L -> [1] -> [2] -> [3] -> [5] -> [7] -> [11] -> None
```
  
## Solution
```python
def remove_duplicates(L):
    curr = L
    while curr and curr.next:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return L
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK