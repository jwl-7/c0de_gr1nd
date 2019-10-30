# Compute the Integer Square Root
Write a program which takes a nonnegative integer and returns the largest integer whose square is less than or equal to the given integer.

## Examples
```
 Input: 11
Output: 3

 Input: 59
Output: 7
```

## Solution
```python
def square_root(k):
    left = 0
    right = k
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1
```

## Explanation
* BLANK

## Code Dissection
1. BLANK