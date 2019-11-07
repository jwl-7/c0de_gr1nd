# Remove First-Name Duplicates
Given an array of elements in the form (first-name, last-name), remove all first-name duplicates.

## Example
```
 Input: [['Foo', '1'], ['ABC', '1'], ['Foo', '1']]
Output: [['ABC', '1'], ['Foo', '1']]
```

## Solution
```python
def eliminate_duplicate(A):
    A.sort()
    idx = 1
    for x in A[1:]:
        if x != A[idx-1]:
            A[idx] = x
            idx += 1
    del A[:idx]
```

## Explanation
* BLANK

## Code Dissection
1. BLANK