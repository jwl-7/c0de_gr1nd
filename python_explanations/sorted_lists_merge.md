# Merge Two Sorted Lists
Consider two singly linked lists in which each node holds a number. Assume the lists are sorted, i.e., numbers in the lists appear in ascending order within each list. The _merge_ of the two lists is a list consisting of the nodes of the two lists in which numbers appear in ascending order.  
  
Write a program that takes two lists, assumed to be sorted, and returns their merge. The only field your program can change in a node is its next field.
  
## Example
```
 Input: [L1] -> [1] -> [3]
        [L2] -> [2] -> [5] -> [7]
Output:  [1] -> [2] -> [3] -> [5] -> [7]
```
  
## Solution
```python
def merge_two_sorted_lists(L1, L2):
    tail = head = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next
    tail.next = L1 or L2
    return head.next
```
  
## Explanation
* A 'dummy' node is used to store the result list
* The result list is initially empty with the tail pointing towards the head (dummy node)
* The solution traverses the two lists, appending the node containing the smaller value to the result list
* Note that the result list is being built using existing nodes and is not copying them
  
## Code Dissection
1. BLANK