# Add List-Based Integers
Write a program which takes two singly linked lists of digits, and returns the list corresponding to the sum of the integers they represent. The least significant digit comes first.
  
## Example
```
 Input: L1 -> [3] -> [2] -> [1] -> None
        L2 -> [5] -> [4] -> [3] -> None
Output:  L -> [8] -> [6] -> [4] -> None
```
  
## Solution
```python
def add_two_numbers(L1, L2):
    dummy = tail = ListNode()
    num = 0
    while L1 or L2 or num:
        if L1:
            num += L1.data
            L1 = L1.next
        if L2:
            num += L2.data
            L2 = L2.next
        tail.next = ListNode(num % 10)
        tail = tail.next
        num //= 10
    return dummy.next
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK