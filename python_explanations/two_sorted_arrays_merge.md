# Merge Two Sorted Arrays
Given two sorted arrays of integers _A_ and _B_, merge _B_ into _A_ as one sorted array.

## Example
```
 Input: A = [-1, 0, 0, 0, 0]
        B = [-3, -1, 0, 3]
        m = 1
        n = 4
Output: [-3, -1, -1, 0, 3]
```

## Solution
```python
def merge_two_sorted_arrays(A, m, B, n):
    while m and n:
        if A[m-1] > B[n-1]:
            A[m+n-1] = A[m-1]
            m -= 1
        else:
            A[m+n-1] = B[n-1]
            n -= 1
    while n:
        A[m+n-1] = B[n-1]
        n -= 1
```

## Pythonic Solution
```python
def merge_two_sorted_arrays_pythonic(A, m, B, n):
    A[m:] = B
    A.sort()
```

## Explanation
* We know there are _m_ elements in _A_ and _n_ elements in _B_
* Array _A_ is filled from the back at index [_m_ + _n_ - 1] with the largest elements from _A_ and _B_

## Code Dissection
1. BLANK

## Pythonic Code Dissection
1. BLANK