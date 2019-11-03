# Reverse a Single Sublist
Given a linked list _L_ and two integers _s_ and _f_, reverse the order of the nodes from _s_ to _f_.

## Example
```
s = 2
f = 4

 Input: L -> [1] -> [2] -> [3] -> [4] -> [5] -> None
Output: L -> [1] -> [4] -> [3] -> [2] -> [7] -> None
```

## Solution
```python
def reverse_sublist(L, start, finish):
    dummy = subhead = ListNode()
    dummy.next = L

    for _ in range(1, start):
        subhead = subhead.next
    subtail = subhead.next

    for _ in range(start, finish):
        tmp = subhead.next
        subhead.next = subtail.next
        subtail.next = subtail.next.next
        subhead.next.next = tmp
    return dummy.next
```

## Explanation
* The strategy is to iterate to the start of the sublist (*s*th node), then reverse the nodes until we reach the end of the sublist (*f*th node)
* Since we do not want to allocate additional nodes and ideally perform the reversal process in one pass, the best approach to this problem is to switch the pointers around rather than the data in the nodes
* The solution uses a dummy head and 3 pointers:
    1. dummy head &mdash; initialized to the head of the list
    2. subhead pointer &mdash; points to the start of the sublist
    3. subtail pointer &mdash; points at the end of the sublist
    4. tmp pointer &mdash; points at the node after the start of the sublist

## Code Dissection
1. Initialize a dummy head that points at the start of the list with a pointer to iterate through the list
    ```python
    dummy = subhead = ListNode()
    dummy.next = L
    ```
2. Iterate through the list using the subhead pointer until we reach the start of the sublist
    ```python
    for _ in range(1, start):
        subhead = subhead.next
    ```
    * Remember that the head of the sublist is the node before we start the reversal process
3. Set a pointer for the end of the sublist
    ```python
    subtail = subhead.next
    ```
    * Since we are reversing the sublist, subhead is initialized to the first node after subhead
4. Start the reversal process and iterate until we reach the end of the sublist
    ```python
    for _ in range(start, finish):
    ```
5. Initialize a pointer to the node after subhead
    ```python
    tmp = subhead.next
    ```
    * This pointer is used to keep track of the node after subhead
6. Set the subhead node to point to the node after the subhead node using the next pointers
    ```python
    subhead.next = subtail.next
    ```
    * This switches the node that comes after subhead
    * Note that we are not modifying the subhead and subhead pointers
7. Set the subhead node to point to the node after the next node
    ```python
    subtail.next = subtail.next.next
    ```
    * This switches the node that comes after subhead
8. Set the subhead node to point to the node at the _tmp_ pointer
    ```python
    subhead.next.next = tmp
    ```
    * This statement reconnects the two nodes we just swapped
    * The result is that the subhead node has been moved over one position
9. After the reversal process is done, return the list
    ```python
    return dummy.next
    ```

## Step-by-Step Example
<img src='drawio_diagrams/reverse_sublist.svg' width='100%'>