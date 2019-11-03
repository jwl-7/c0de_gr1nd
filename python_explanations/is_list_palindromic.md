# Test Whether a Singly Linked List Is Palindromic
Given a singly linked list, return whether or not it is palindromic.

## Examples
```
 Input: L -> [7] -> [3] -> [1] -> [3] -> [7] -> None
Output: True

 Input: L -> [1] -> [2] -> [3] -> [4] -> None
Output: False
```

## Solution
```python
def reverse_linked_list(head):
    prev = None
    curr = head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


def is_linked_list_a_palindrome(L):
    slow = fast = L
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next

    a = L
    b = reverse_linked_list(slow)

    while b:
        if a.data != b.data:
            return False
        a = a.next
        b = b.next
    return True
```

## Explanation
1. Find the second half of the list using a slow pointer and a fast pointer
2. Reverse the second half of the list
3. Compare the nodes in the first half to the nodes in the second half
* If the data in each node in the first half matches the data in each node in the second half, then the list is a palindrome
* When the fast pointer hits the end of the list, the slow pointer will be the head of the second half

## Code Dissection - reverse_linked_list
1. Initialize a previous and current pointer
    ```python
    prev = None
    curr = head
    ```
2. Loop until the current pointer hits the end of the list
    ```python
    while curr:
    ```
3. Store the next node, then set the current node to point at the previous node
    ```python
    nxt = curr.next
    curr.next = prev
    ```
4. Move the previous pointer and current pointer 1 step forward
    ```python
    prev = curr
    curr = nxt
    ```
5. Return the head of the reversed list
    ```python
    return prev
    ```

## Code Dissection - is_linked_list_a_palindrome
1. Initialize a slow and fast pointer to the head of the list
    ```python
    slow = fast = L
    ```
2. Move the slow pointer 1 step and the fast pointer 2 steps at a time until the fast pointer hits the end of the list
    ```python
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    ```
3. Set a pointer at the first half of the list and a pointer at the second half of the list reversed
    ```python
    a = L
    b = reverse_linked_list(slow)
    ```
4. Move pointers _a_ and _b_ 1 step at a time to compare the data of each node in the first half to the second half
    ```python
    while b:
        if a.data != b.data:
            return False
        a = a.next
        b = b.next
    ```
5. If the data in each node is the same after the _b_ pointer hits the end of the second half, then the list is palindromic
    ```python
    return True
    ```