# The 3-Sum Problem
Given an array _A_ of numbers and a target number _t_, determine if there are 3 numbers in _A_ that add up to _t_.

## Examples
```
 Input: A = [2, 3, 5, 7, 11]
        t = 21
Output: True

11 + 7 + 3 = 21


 Input: A = [1, -5, 5, -1, 3, -4]
        t = 12
Output: False
```

## Solution
```python
def has_two_sum(A, t):
    i = 0
    j = len(A) - 1
    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1
    return False


def has_three_sum(A, t):
    A.sort()
    return any(has_two_sum(A, t - x) for x in A)
```

## Explanation
* BLANK

## Code Dissection
1. BLANK