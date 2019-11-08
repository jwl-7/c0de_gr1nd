# Implement a Fast Sorting Algorithm for Lists
Given a linked list, sort it fast.

## Example
```
 Input: L -> [3] -> [3] -> [-2] -> [1] -> [-2] -> [-2] -> None
Output: L -> [-2] -> [-2] -> [-2] -> [1] -> [3] -> [3] -> None
```

## Solution
```python
def stable_sort_list(L):
    if not L or not L.next:
        return L

    prev = None
    slow = fast = L
    while fast and fast.next:
        prev = slow
        fast = fast.next.next
        slow = slow.next
    prev.next = None

    sorted_l1 = stable_sort_list(L)
    sorted_l2 = stable_sort_list(slow)
    return merge_two_sorted_lists(sorted_l1, sorted_l2)
```

## Explanation
* For an explanation on merging two sorted lists: [Merge Two Sorted Lists](#sorted_lists_merge.md)
* The solution implements a merge sort

## Code Dissection
1. Set the base case: L is empty or a single node
    ```python
    if not L or not L.next:
        return L
    ```
2. Using a slow and fast pointer, find the midpoint of the list
    ```python
    prev = None
    slow = fast = L
    while fast and fast.next:
        prev = slow
        fast = fast.next.next
        slow = slow.next
    ```
3. Split the list into two parts
    ```python
    prev.next = None
    ```
4. Create the two half lists
    ```python
    sorted_l1 = stable_sort_list(L)
    sorted_l2 = stable_sort_list(slow)
    ```
5. Merge the two parts and return the sorted list
    ```python
    return merge_two_sorted_lists(sorted_l1, sorted_l2)
    ```