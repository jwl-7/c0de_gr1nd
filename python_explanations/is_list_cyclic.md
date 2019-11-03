# Test for Cyclicity
Given a linked list, determine whether or not it contains a cycle.

## Examples
<img src='drawio_diagrams/is_list_cyclic1.svg' width='40%'>

```
 Input: [1, 5, 7]
Output: None
```

<img src='drawio_diagrams/is_list_cyclic2.svg' width='60%'>

```
 Input: [1, 2, 3, 4]
Output: 2
```

## Solution
```python
def has_cycle(head):
    slow = fast = head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            fast = head
            while fast is not slow:
                fast = fast.next
                slow = slow.next
            return fast
    return None
```

## Explanation
* The solution uses [Floyd's cycle-finding algorithm](https://en.wikipedia.org/wiki/Cycle_detection#Floyd's_Tortoise_and_Hare)
* Imagine a slow and fast runner racing around a circular track &mdash; the fast runner will eventually meet the slow runner
* For checking if the list is cyclic, we use two pointers and if they meet, the list contains a cycle
    1. The slow pointer &mdash; moves 1 step at a time
    2. The fast pointer &mdash; moves 2 steps at a time
* If there is a cycle: after the two pointers meet, the start of the cycle can be found by setting a pointer at the head and iterating both slow pointers at the same time until they meet
* If there is not a cycle in the list, the fast pointer will eventually reach the end of the list

## Code Dissection
1. Initialize a slow and fast pointer to the head
    ```python
    slow = fast = head
    ```
2. Iterate both pointers through the list until the fast pointer reaches the end of the list
    ```python
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
    ```
    * The fast pointer moves 2 steps at a time
    * The slow pointer moves 1 step at a time
    * The fast pointer will reach the end of the list if there is no cycle
3. If the two pointers meet and the list is cyclic, find the start of the cycle and return it
    ```python
    if fast is slow:
        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast
    ```
    * When finding the start of the cycle, the fast pointer and slow pointer both move 1 step at a time
    * The start of the cycle is found when the two pointers meet
4. If the list is not cyclic, return None
    ```python
    return None
    ```