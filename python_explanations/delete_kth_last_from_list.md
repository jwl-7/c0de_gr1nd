# Remove the *k*th Last Element from a List
Given a singly linked list and an integer _k_, write a program to remove the *k*th last element from the list. Your algorithm cannot use more than a few words of storage, regardless of the length of the list. In particular, you cannot assume that it is possible to record the length of the list.
  
## Example
```
 Input: L = [1] -> [2] -> [3] -> [4] -> [5] -> None
        k = 2
Output: [1] -> [2] -> [3] -> [5] -> None
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
* The solution uses two pointers to traverse the list:
    1. First, the _fast_ pointer moves _k_ steps
    2. Then, the _slow_ pointer and the _fast_ pointer move one step at a time until the _fast_ pointer reaches the tail of the list
* When the _fast_ pointer is at the tail of the list, the _slow_ pointer is at the (_k_ + 1)th last node
* If the _fast_ pointer is at the tail of the list before iterating the _slow_ pointer, then it is the head node that needs to be removed
  
## Code Dissection
1. Initialize a _slow_ and _fast_ pointer to the head of the list
    ```python
    slow = fast = L
    ```
2. Iterate the _fast_ pointer _k_ steps
    ```python
    for _ in range(k):
        fast = fast.next
    ```
3. If the _fast_ pointer is at the tail of the list, remove the head
    ```python
    if not fast:
        return L.next
    ```
4. Iterate the _slow_ and _fast_ pointer until the _fast_ pointer reaches the tail
    ```python
    while fast.next:
        fast = fast.next
        slow = slow.next
    ```
5. Remove the *k*th node from the end of the list
    ```python
    slow.next = slow.next.next
    ```
6. Return the head of the list
    ```python
    return L
    ```