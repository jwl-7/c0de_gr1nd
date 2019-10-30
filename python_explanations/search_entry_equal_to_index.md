# Search a Sorted Array for Entry Equal to Its Index
Design an efficient algorithm that takes a sorted array of distinct integers, and returns an index _i_ such that the element at index _i_ equals _i_.

## Examples
```
 Input: [-2, 0, 1, 3]
Output: 3

 Input: [-2, -1, 0, 2, 4, 5]
Output: 4 or 5
```

## Solution
```python
def search_entry_equal_to_its_index(A):
    left = 0
    right = len(A) - 1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] < mid:
            left = mid + 1
        elif A[mid] > mid:
            right = mid - 1
        else:
            return mid
    return -1
```

## Explanation
* BLANK

## Code Dissection
1. BLANK