# Find the Min and Max Simultaneously
Given an array of comparable objects, you can find either the _min_ or the _max_ of the elements in the array with _n_ - 1 comparisons, where _n_ is the length of the array.

Design an algorithm to find the min and max elements in an array.

## Examples
```
 Input: [1, 2, 3, 4, 5]
Output: (1, 5)

 Input: [5, -4, -6, 5, -3, 7, 5, -3]
Output: (-6, 7)
```

## Solution
```python
MinMax = collections.namedtuple('MinMax', ('smallest', 'largest'))


def find_min_max(A):
    if len(A) % 2 == 0:
        minimum = min(A[0], A[1])
        maximum = max(A[0], A[1])
        i = 2
    else:
        minimum = maximum = A[0]
        i = 1
    while i < len(A) - 1:
        if A[i] < A[i+1]:
            minimum = min(minimum, A[i])
            maximum = max(maximum, A[i+1])
        else:
            minimum = min(minimum, A[i+1])
            maximum = max(maximum, A[i])
        i += 2
    return MinMax(minimum, maximum)
```

## Explanation
* BLANK

## Code Dissection
1. BLANK