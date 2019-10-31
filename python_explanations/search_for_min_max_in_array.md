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
* The _min_ and _max_ are computed in pairs, obviously, but its the initial _min_ and _max_ that really helps the algorithm
* If _n_ is odd, then set _min_ and _max_ as the first element
* If _n_ is even, then set _min_ and _max_ as the minimum and maximum of the first two elements respectively

## Code Dissection
1. If _n_ is even, then set _min_ and _max_ as the minimum and maximum of the first two elements respectively
    ```python
    if len(A) % 2 == 0:
        minimum = min(A[0], A[1])
        maximum = max(A[0], A[1])
        i = 2
    ```
2. If _n_ is odd, then set _min_ and _max_ as the first element
    ```python
    else:
        minimum = maximum = A[0]
        i = 1
    ```
3. Loop over each element in pairs, and compare each pair to decide how to compare the _min_ and _max_
    ```python
    while i < len(A) - 1:
        if A[i] < A[i+1]:
            minimum = min(minimum, A[i])
            maximum = max(maximum, A[i+1])
        else:
            minimum = min(minimum, A[i+1])
            maximum = max(maximum, A[i])
        i += 2
    ```
4. Return the _min_ and _max_ in a tuple
    ```python
    return MinMax(minimum, maximum)
    ```