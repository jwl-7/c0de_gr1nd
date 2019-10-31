# Compute the Real Square Root
Implement a function which takes as input a floating point value and returns its square root.

## Examples
```
 Input: 1024.0
Output: 31.999999971129

 Input: 74904312.285
Output: 8654.72774144241
```

## Solution
```python
def square_root(x):
    left = x if x < 1.0 else 1.0
    right = 1.0 if x < 1.0 else x
    while not math.isclose(left, right):
        mid = (left + right) / 2
        if mid * mid <= x:
            left = mid
        else:
            right = mid
    return left
```

## Explanation
* BLANK

## Code Dissection
1. BLANK