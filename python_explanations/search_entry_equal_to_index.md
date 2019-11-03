# Search a Sorted Array for Entry Equal to Its Index
Given an array _A_ of distinct integers, return an index _i_ such that _A_[_i_] = _i_.

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
* The solution uses the iterative implementation of a binary search

## Code Dissection
1. Set a left and right pointer at the start and end of the array respectively
    ```python
    left = 0
    right = len(A) - 1
    ```
2. Loop until the left and right pointer pass each other
    ```python
    while left <= right:
    ```
3. Compute the mid pointer
    ```python
    mid = (left + right) // 2
    ```
4. Check if _k_ is at _mid_
    ```python
    if A[mid] < mid:
        left = mid + 1
    elif A[mid] > mid:
        right = mid - 1
    else:
        return mid
    ```
5. There is no index _i_ that equals _i_
    ```python
    return -1
    ```