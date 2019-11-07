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
    while m > 0 and n > 0:
        if A[m-1] > B[n-1]:
            A[m+n-1] = A[m-1]
            m -= 1
        else:
            A[m+n-1] = B[n-1]
            n -= 1
    while n > 0:
        A[m+n-1] = B[n-1]
        n -= 1
```

## Explanation
* BLANK

## Code Dissection
1. BLANK