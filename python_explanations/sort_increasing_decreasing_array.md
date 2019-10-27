# Sort an Increasing-Decreasing Array
An array is said to be _k_-increasing-decreasing if elements repeteadly increase up to a certain index after which they decrease, then again increase, a total of _k_ times.

Design an efficient algorithm for sorting a *k*-increasing-decreasing array.

## Examples
```
 Input: [1, 2, 3, 2, 1, 4, 5, 10, 9, 4, 4, 1, -1]
Output: [-1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 9, 10]

 Input: [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
Output: [57, 131, 190, 221, 294, 339, 418, 442, 452, 493]
```

## Solution
```python
def sort_k_increasing_decreasing_array(A):
    sub_arrays = []
    increasing = True
    start = 0
    for i in range(1, len(A)):
        if A[i] >= A[i-1] and not increasing:
            sub_arrays.append(A[i-1:start-1:-1])
            increasing = True
            start = i
        elif A[i] < A[i-1] and increasing:
            sub_arrays.append(A[start:i])
            increasing = False
            start = i
        if i == len(A) - 1:
            if not increasing:
                sub_arrays.append(A[:start-1:-1])
            else:
                sub_arrays.append(A[start:])
    return list(heapq.merge(*sub_arrays))
```

## Explanation
* BLANK

## Code Dissection
1. BLANK