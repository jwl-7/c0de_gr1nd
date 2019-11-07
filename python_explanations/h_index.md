# Computing the H-Index
Given an array of citations (nonnegative integers), find the [h-index](https://en.wikipedia.org/wiki/H-index).

## Examples
```
 Input: [0, 2, 3, 1, 4]
Output: 2

 Input: [0, 21, 14, 15, 16, 19, 6, 13, 20, 13, 24, 15, 7]
Output: 10
```

## Solution
```python
def h_index(citations):
    n = len(citations)
    citations.sort()
    for i, c in enumerate(citations):
        if c >= n - i:
            return n - i
    return 0
```

## Explanation
* BLANK

## Code Dissection
1. BLANK