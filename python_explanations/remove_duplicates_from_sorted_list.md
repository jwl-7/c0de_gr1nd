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
* While traversing the list, all successive nodes with the same value as the current node are removed
  
## Code Dissection
1. Initialize a pointer to the head of the list
    ```python
    curr = L
    ```
2. Iterate the pointer until the end of the list
    ```python
    while curr and curr.next:
    ```
3. If the current node contains the same value as the next node, remove it
    ```python
    if curr.data == curr.next.data:
        curr.next = curr.next.next
    ```
4. If the next node is not a duplicate, move the pointer to the next node
    ```python
    else:
        curr = curr.next
    ```
5. Return the list with the duplicates removed
    ```python
    return L
    ```