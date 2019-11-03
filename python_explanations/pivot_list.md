# Implement List Pivoting
Given a singly linked list and an integer _k_, rearrange the elements in the order:
1. Nodes w/ data < _k_
2. The node w/ _k_
3. Nodes w/ data > _k_

## Example
```
x = 7

 Input: L -> [3] -> [2] -> [2] -> [11] -> [7] -> [5] -> [11] -> None
Output: L -> [3] -> [2] -> [2] -> [5] -> [7] -> [11] -> [11] -> None
```

## Solution
```python
def list_pivoting(L, x):
    less_head = less = ListNode()
    equal_head = equal = ListNode()
    greater_head = greater = ListNode()
    while L:
        if L.data < x:
            less.next = L
            less = less.next
        elif L.data == x:
            equal.next = L
            equal = equal.next
        elif L.data > x:
            greater.next = L
            greater = greater.next
        L = L.next
    greater.next = None
    equal.next = greater_head.next
    less.next = equal_head.next
    return less_head.next
```

## Explanation
* The solution appends nodes from the original lists to 3 separate lists:
    1. The less list &mdash; nodes with values less than _x_
    2. The equal list &mdash; nodes with values equal to _x_
    3. The greater list &mdash; nodes with values greater than _x_
* After the 3 lists are built, they are connected together to perform the pivoted list

## Code Dissection
1. Create the 3 lists with tail pointers
    ```python
    less_head = less = ListNode()
    equal_head = equal = ListNode()
    greater_head = greater = ListNode()
    ```
2. Loop until the original list is empty and append nodes to their respective lists
    ```python
    while L:
        if L.data < x:
            less.next = L
            less = less.next
        elif L.data == x:
            equal.next = L
            equal = equal.next
        elif L.data > x:
            greater.next = L
            greater = greater.next
        L = L.next
    ```
3. Set the end of the pivoted list to None
    ```python
    greater.next = None
    ```
4. Connect the equal list to the greater list
    ```python
    equal.next = greater_head.next
    ```
5. Connect the less list to the equal list
    ```python
    less.next = equal_head.next
    ```
6. Return the pivoted list
    ```python
    return less_head.next
    ```