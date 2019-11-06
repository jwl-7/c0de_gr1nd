# Find the Length of a Longest Contained Interval
Given an array of integers, find the length of the longest consecutive subsequence.

## Examples
```
   Input: [2, 3, 1, 5]
  Output: 3
Sequence: [2, 3, 1]

   Input: [1, 7, 3, 6, 4, 20, 2]
  Output: 4
Sequence: [1, 3, 4, 2]
```

## Solution
```python
def longest_contained_range(A):
    A = set(A)
    longest = 0
    for x in A:
        if x - 1 not in A:
            y = x + 1
            while y in A:
                y += 1
            longest = max(longest, y - x)
    return longest
```

## Explanation
* BLANK

## Code Dissection
1. BLANK