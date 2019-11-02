# Find the Duplicate and Missing Elements
You are given an array of _n_ integers, each between 0 and _n_ - 1, inclusive. Exactly one element appears twice, implying that exactly one number between 0 and _n_ - 1 is missing from the array. How would you compute the duplicate and missing numbers?

## Example
```
 Input: [0, 1, 2, 3, 4, 4, 5, 6, 7, 8, 9]
Output: (duplicate=4, missing=10)
```

## Solution
```python
DuplicateAndMissing = collections.namedtuple('DuplicateAndMissing', ('duplicate', 'missing'))


def find_duplicate_missing(A):
    x = A[0]
    y = 0
    for i in range(1, len(A)):
        x ^= A[i] ^ i

    set_bit = x & ~(x - 1)
    for i, num in enumerate(A):
        if i & set_bit:
            y ^= i
        if num & set_bit:
            y ^= num

    x ^= y
    if y in A:
        return DuplicateAndMissing(y, x)
    else:
        return DuplicateAndMissing(x, y)
```

## Explanation
* BLANK

## Code Dissection
1. BLANK