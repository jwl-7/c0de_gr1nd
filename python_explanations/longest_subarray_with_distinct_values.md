# Find the Longest Subarray with Distinct Entries
Given an array, return the length of the longest subarray with distinct elements.

## Examples
```
 Input: ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'g']
Output: 4

 Input: [1, 1, 2, 3, 4, 5, 5, 6]
Output: 5
```

## Solution
```python
def longest_subarray_with_distinct_entries(A):
    recent = {}
    result = 0
    start = 0
    for i, s in enumerate(A):
        if s not in recent or recent[s] < start:
            result = max(result, i - start + 1)
        else:
            start = recent[s] + 1
        recent[s] = i
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK