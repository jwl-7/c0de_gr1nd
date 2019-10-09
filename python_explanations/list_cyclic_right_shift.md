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
1. Find the tail and the length of the list
2. Make the list circular
3. Rotate the list so that the head becomes the (_n_ - _k_)th node
4. Disconnect the circular link
* If _k_ is larger than _n_(the number of nodes in the list), it is equivalent to shift the list by _k_ mod _n_
  
## Code Dissection
1. Initializer a pointer to the head of the list and a variable for counting the nodes
    ```python
    tail = L
    n = 1
    ```
2. Traverse the list to find the tail and count the number of nodes to get the length
    ```python
    while tail.next:
        tail = tail.next
        n += 1
    ```
3. Just in case _k_ is larger than _n_, compute _k_ mod _n_
    ```python
    k %= n
    ```
4. If _k_ is equal to zero, then no shifts are needed, and we return the head
    ```python
    if k == 0:
        return L
    ```
5. Connect the tail to the head to make the list circular
    ```python
    tail.next = L
    ```
6. Rotate the list by shifting the tail _n_ - _k_ steps
    ```python
    for _ in range(n - k):
        tail = tail.next
    ```
7. Set the head as the (_n_ - _k_)th node in the list
    ```python
    tail.next = None
    ```
8. Disconnect the tail to remove the circular link
    ```python
    tail.next = None
    ```
9. Return the cyclically shifted list
    ```python
    return L
    ```