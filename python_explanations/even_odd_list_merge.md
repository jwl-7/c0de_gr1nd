# Implement Even-Odd Merge
Consider a singly linked list whose nodes are numbered starting at 0. Define the even-odd merge of the list to be the list of the even-numbered nodes followed by the odd-numbered nodes.

Write a program that computes the even-odd merge.

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
    1. The _even_ pointer, which starts at the head of the list
    2. The _odd_ pointer, which starts at the node after the head (which will also be the *odd_head*)
* As we traverse through the list, the _even_ and _odd_ next pointers are used to connect nodes to an even and odd list respectively
* The two lists are merged by connecting the tail of the even list to the head of the odd list
* The original list head is not touched and will be the head of the even-odd list

## Code Dissection
1. Check if the list is empty
    ```python
    if not L:
        return L
    ```
2. Initialize an _even_ pointer to the head and an _odd_ and *odd_head* pointer to the next node
    ```python
    even = L
    odd = odd_head = even.next
    ```
3. Traverse until _odd_ pointer hits the end of the list
    ```python
    while odd and odd.next:
    ```
4. Set the _even_ next pointer to point to the next even node, and set the _odd_ next pointer to point to the next odd node
    ```python
    even.next = even.next.next
    odd.next = odd.next.next
    ```
5. Move the _even_ and _odd_ pointer to the next even and odd nodes respectively
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