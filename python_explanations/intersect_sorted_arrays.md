# Compute the Intersection of Two Sorted Arrays
Given two sorted arrays, find their union.

## Examples
```
 Input: [1, 2, 3, 4]
        [1, 4, 5]
Output: [1, 4]

 Input: [-2, 2, 2, 3, 4]
        [-6, -3, -1, 0, 1, 3, 4]
Output: [3, 4]
```

## Solution
```python
def intersect_two_sorted_arrays(A, B):
    return sorted(set(A) & set(B))
```

## Explanation
* Using `set()` removes the duplicates
* The bitwise and operator `&` computes the intersection
* `sorted()` is necessary for the result to be in order, but it can slow the solution down

## Code Dissection
1. Return the intersection of two sorted arrays
    ```python
    return sorted(set(A) & set(B))
    ```