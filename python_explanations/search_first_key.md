# Search a Sorted Array for First Occurrence of _k_
Write a method that takes a sorted array and a key and returns the index of the _first_ occurrence of that key in the array. Return -1 if the key does not appear in the array.

## Examples
```
 Input: k = 4
        [0, 1, 2, 3, 4, 5, 6, 7]
Output: 4

 Input: k = 2
        [0, 0, 0, 1, 1, 1, 1, 1, 2]
Output: 8
```

## Solution
```python
def search_first_of_k(A, k):
    left = 0
    right = len(A) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] == k:
            result = mid
            right = mid - 1
        elif A[mid] < k:
            left = mid + 1
        elif A[mid] > k:
            right = mid - 1
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK