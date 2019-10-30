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
* For any _m_, if _A_[_m_] > _A_[_n_-1], then the minimum value must be an index in the range [_m_+1, _n_-1]
* For any _m_, if _A_[_m_] < _A_[_n_-1], then the minimum value can't be an index in the range [_m_+1, _n_-1]
* It is not possible for _A_[_m_] = _A_[_n_-1]

## Code Dissection
1. Set a left and right pointer at the start and end of the array respectively
    ```python
    left = 0
    right = len(A) - 1
    ```
2. Loop until the left and right pointer meet each other
    ```python
    while left < right:
    ```
3. Compute the mid pointer
    ```python
    mid = (left + right) // 2
    ```
4. Search for the minimum value
    ```python
    if A[mid] > A[right]:
        left = mid + 1
    else:
        right = mid
    ```
5. Return the smallest value
    ```python
    return left
    ```