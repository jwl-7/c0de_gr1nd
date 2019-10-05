# Merge Two Sorted Lists
Consider two singly linked lists in which each node holds a number. Assume the lists are sorted, i.e., numbers in the lists appear in ascending order within each list. The _merge_ of the two lists is a list consisting of the nodes of the two lists in which numbers appear in ascending order.  
  
Write a program that takes two lists, assumed to be sorted, and returns their merge. The only field your program can change in a node is its next field.
  
## Example
```
 Input: [L1] -> [1] -> [3] -> None
        [L2] -> [2] -> [5] -> [7] -> None
Output:  [R] -> [1] -> [2] -> [3] -> [5] -> [7] -> None
```
  
## Solution
```python
def merge_two_sorted_lists(L1, L2):
    dummy = tail = ListNode()
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
        tail = tail.next
    tail.next = L1 or L2
    return dummy.next
```
  
## Explanation
* A 'dummy' head node is used to store the merge list
* The tail is used to traverse and append nodes
* The solution traverses the two lists, appending the node containing the smaller value to the merge list
* When traversing, if one list becomes empty before the other, the rest of the remaining nodes are appended to the merge list
* Note that the merge list is being built using existing nodes and is not copying them
  
## Code Dissection
1. Create a dummy node to store the merge list and a tail
    ```python
    dummy = tail = ListNode()
    ```
    * This statement does not create two separate nodes
2. Traverse the two lists, appending the node containing the smaller value to the merge list
    ```python
    while L1 and L2:
        if L1.data < L2.data:
            tail.next = L1
            L1 = L1.next
        else:
            tail.next = L2
            L2 = L2.next
    ```
    * This loop runs until at least one of the lists becomes empty
    * The tail pointer of the merge list is set to point at the head of the list that contains the correct node
    * The head of that list is set to point at the next node in its list
3. Set _tail_ to the next node, since the tail pointer should always point to the end of a list
    ```python
    tail = tail.next
    ```
4. When at least one of the lists becomes empty, add the remaining nodes to the end of the merge list
    ```python
    tail.next = L1 or L2
    ```
5. Return the merged list
    ```python
    return dummy.next
    ```
  
## Step-by-Step Example
<img src='drawio_diagrams/sorted_lists_merge.svg'>