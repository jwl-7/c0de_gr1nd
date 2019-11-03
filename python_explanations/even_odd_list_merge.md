# Implement Even-Odd Merge
Given a singly linked list, group the even nodes together followed by the odd nodes.

## Examples
```
 Input: L -> [0] -> [1] -> [2] -> [3] -> [4] -> None
Output: L -> [0] -> [2] -> [4] -> [1] -> [3] -> None

 Input: L -> [3] -> [7] -> [6] -> [4] -> [9] -> [2] -> None
Output: L -> [3] -> [6] -> [9] -> [7] -> [4] -> [2] -> None
```

## Solution
```python
def even_odd_merge(L):
    if not L:
        return L
    even = L
    odd = odd_head = even.next
    while odd and odd.next:
        even.next = even.next.next
        odd.next = odd.next.next
        even = even.next
        odd = odd.next
    even.next = odd_head
    return L
```

## Explanation
* The solution uses two pointers to traverse the list:
    1. The even pointer &mdash; starts at the head of the list
    2. The odd pointer &mdash; starts at the node after the head (the odd head)
* As we traverse through the list, the even's and odd's next pointers are used to connect nodes to an even and odd list respectively
* The two lists are merged by connecting the tail of the even list to the head of the odd list
* The original list head is not touched and will be the head of the even-odd list

## Code Dissection
1. Check if the list is empty
    ```python
    if not L:
        return L
    ```
2. Initialize an even pointer to the head of _L_ and an odd pointer/head to the next node
    ```python
    even = L
    odd = odd_head = even.next
    ```
3. Traverse until the odd pointer hits the end of the list
    ```python
    while odd and odd.next:
    ```
4. Set even's next pointer to the next even node, and set odd's next pointer to the next odd node
    ```python
    even.next = even.next.next
    odd.next = odd.next.next
    ```
5. Move the even and odd pointers to the next even and odd nodes respectively
    ```python
    even = even.next
    odd = odd.next
    ```
6. After the even and odd lists are built, connect the tail of the even list to the head of the odd list to merge the two lists
    ```python
    even.next = odd_head
    ```
7. Return the even-odd list
    ```python
    return L
    ```