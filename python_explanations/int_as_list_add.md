# Add List-Based Integers
Write a program which takes two singly linked lists of digits, and returns the list corresponding to the sum of the integers they represent. The least significant digit comes first.

## Example
```
 Input: L1 -> [3] -> [2] -> [1] -> None
        L2 -> [5] -> [4] -> [3] -> None
Output:  L -> [8] -> [6] -> [4] -> None
```

## Solution
```python
def add_two_numbers(L1, L2):
    dummy = tail = ListNode()
    num = 0
    while L1 or L2 or num:
        if L1:
            num += L1.data
            L1 = L1.next
        if L2:
            num += L2.data
            L2 = L2.next
        tail.next = ListNode(num % 10)
        tail = tail.next
        num //= 10
    return dummy.next
```

## Explanation
* Since the least significant digit comes first, that means the digits are in reverse order
* The solution is based off the grade-school algorithm for addition, which is to compute the sum of the digits in the corresponding nodes in the two lists while handling the carry-out

## Code Dissection
1. Create a dummy node that will point to the sum list and a variable for use with the addition
    ```python
    dummy = tail = ListNode()
    num = 0
    ```
2. Loop while there is still a value in _L1_ or _L2_ or _num_
    ```python
    while L1 or L2 or num:
    ```
3. Add the data in the two corresponding nodes in the two lists to _num_
    ```python
    if L1:
        num += L1.data
        L1 = L1.next
    if L2:
        num += L2.data
        L2 = L2.next
    ```
4. Append a node to the sum list with the carry-in digit of _num_
    ```python
    tail.next = ListNode(num % 10)
    ```
5. Move _tail_ to the next node and set _num_ to the carry-out digit
    ```python
    tail = tail.next
    num //= 10
    ```
6. Return the sum list
    ```python
    return dummy.next
    ```