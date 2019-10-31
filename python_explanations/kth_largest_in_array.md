# Find the *k*th Largest Element
Design an algorithm for computing the *k*th largest element in an array.

## Examples
```
 Input: k = 2
        [2, -2, 1]
Output: 1

 Input: k = 7
        [3, -5, -3, 3, 3, 2, -8, -3]
Output: -5
```

## Solution
```python
def find_kth_largest(k, A):
    left = 0
    right = len(A) - 1
    while left <= right:
        pivot = partition(A, left, right)
        if pivot == k - 1:
            return A[pivot]
        elif pivot < k - 1:
            left = pivot + 1
        else:
            right = pivot - 1


def partition(A, left, right):
    pivot_idx = random.randint(left, right)
    pivot_val = A[pivot_idx]
    new_pivot = left
    A[pivot_idx], A[right] = A[right], A[pivot_idx]
    for i in range(left, right):
        if A[i] > pivot_val:
            A[i], A[new_pivot] = A[new_pivot], A[i]
            new_pivot += 1
    A[right], A[new_pivot] = A[new_pivot], A[right]
    return new_pivot
```

## Explanation
* BLANK

## Code Dissection
1. BLANK