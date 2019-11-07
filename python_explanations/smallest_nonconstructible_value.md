# Smallest Nonconstructible Value
Given an array of positive integers, find the smallest integer that cannot be represented as the sum of any subset of the array.

## Examples
```
 Input: [1, 2, 3, 4]
Output: 11

 Input: [1, 2, 6, 10, 11, 15]
Output: 4
```

## Solution
```python
def smallest_nonconstructible_value(A):
    A.sort()
    x = 1
    for num in A:
        if num <= x:
            x += num
        else:
            break
    return x
```

## Explanation
* BLANK

## Code Dissection
1. BLANK