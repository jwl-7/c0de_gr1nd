# Find Smallest Subarray Sequentially Covering All Values
Given an array of strings and a set of strings, return the starting/ending indices of the shortest subarray that contains the set. The strings in the subarray must occur in sequential order.

## Examples
```
 Input: paragraph = ['a', 'b', 'd', 'f', 'g', 'c', 'a', 'd']
         keywords = ['a', 'b', 'c']
Output: Subarray(start=0, end=5)

 Input: paragraph = ['dog', 'cat', 'dog', 'banana', 'cat', 'dog']
         keywords = ['banana', 'cat', 'dog']
Output: Subarray(start=3, end=5)
```

## Solution
```python
def find_smallest_sequentially_covering_subset(paragraph, keywords):
    key_lookup = {}
    for i, s in enumerate(keywords):
        key_lookup[s] = i
    recent = [-1] * len(keywords)
    smallest = [float('inf')] * len(keywords)
    shortest = float('inf')
    start, end = 0, 0

    for i, s in enumerate(paragraph):
        if s in key_lookup:
            key_idx = key_lookup[s]
            if key_idx == 0:
                smallest[key_idx] = 1
            elif smallest[key_idx - 1] != float('inf'):
                prev_dist = i - recent[key_idx - 1]
                smallest[key_idx] = prev_dist + smallest[key_idx - 1]
            recent[key_idx] = i
            if key_idx == len(keywords) - 1 and smallest[-1] < shortest:
                shortest = smallest[-1]
                start, end = i - shortest + 1, i
    return Subarray(start, end)
```

## Explanation
* BLANK

## Code Dissection
1. BLANK