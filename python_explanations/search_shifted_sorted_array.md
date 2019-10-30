# Search a Cyclically Sorted Array
An array is said to be cyclically sorted if it is possible to cyclically shift its entries so that it becomes sorted.

Design an _O(logn)_ algorithm for finding the position of the smallest element in a cyclically sorted array. Assume all elements are distinct.

## Examples
```
 Input: [16, 2, 4, 8]
Output: 1

 Input: [2, 3, -5, -2, -1, 0]
Output: 2
```

## Solution
```python
def search_smallest(A):
    left = 0
    right = len(A) - 1
    while left < right:
        mid = (left + right) // 2
        if A[mid] > A[right]:
            left = mid + 1
        else:
            right = mid
    return left
```

## Explanation
* BLANK

## Code Dissection
1. BLANK