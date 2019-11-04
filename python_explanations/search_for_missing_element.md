# Find the Duplicate and Missing Elements
Given an array of _n_ numbers, each between 0 and _n_ - 1, find the missing number and the duplicate number.

## Example
```
 Input: [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
Output: DuplicateAndMissing(duplicate=4, missing=10)
```

## Solution
```python
DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))


def find_duplicate_missing(A):
    x = A[0]
    y = 0
    for i in range(1, len(A)):
        x ^= A[i] ^ i

    set_bit = x & ~(x - 1)
    for i, num in enumerate(A):
        if i & set_bit:
            y ^= i
        if num & set_bit:
            y ^= num

    x ^= y
    if y in A:
        return DuplicateAndMissing(y, x)
    else:
        return DuplicateAndMissing(x, y)
```

## Explanation
1. XOR all the array elements &mdash; _x_
2. XOR the result with all numbers from 1 to _n_ &mdash; _x_
3. Get the rightmost set bit of _x_
4. Compare the set bit (position) to all the indexes/elements in the array &mdash; _y_
5. XOR _x_ with _y_
6. If _y_ is in the array, then it is the duplicate, else, it is the missing element

## Code Dissection
1. Let _x_ and _y_ be variables to store the duplicate/missing element
    ```python
    x = A[0]
    y = 0
    ```
2. XOR all the array elements, and xor that result w/ all numbers from 1 to _n_
    ```python
    for i in range(1, len(A)):
        x ^= A[i] ^ i
    ```
3. Get the rightmost set bit of _x_
    ```python
    set_bit = x & ~(x - 1)
    ```
4. Find entries/numbers where the *set_bit* position is 1
    ```python
    for i, num in enumerate(A):
        if i & set_bit:
            y ^= i
        if num & set_bit:
            y ^= num
    ```
5. XOR _x_ with _y_
    ```python
    x ^= y
    ```
6. If _y_ is in the array, then it is the duplicate, else, it is the missing element
    ```python
    if y in A:
        return DuplicateAndMissing(y, x)
    else:
        return DuplicateAndMissing(x, y)
    ```