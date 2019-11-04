# Find the Smallest Subarray Covering All Values
Given an array of strings and a set of strings, return the starting/ending indices of the shortest subarray that contains the set.

## Examples
```
 Input: paragraph = ['a', 'b', 'd', 'f', 'g', 'c', 'a', 'd']
         keywords = ['a', 'b', 'c']
Output: Subarray(start=0, end=5)

 Input: paragraph = ['dog', 'cat', 'dog', 'banana', 'cat', 'dog']
         keywords = ['banana', 'cat', 'dog']
Output: Subarray(start=1, end=3)
```

## Solution
```python
Subarray = collections.namedtuple('Subarray', ('start', 'end'))


def find_smallest_subarray_covering_set(paragraph, keywords):
    need = collections.Counter(keywords)
    missing = len(keywords)
    start, end = 0, 0
    i = 0
    for j, s in enumerate(paragraph):
        missing -= need[s] > 0
        need[s] -= 1
        if not missing:
            while need[paragraph[i]] < 0:
                need[paragraph[i]] += 1
                i += 1
            if not end or j - i < end - start:
                start, end = i, j
            need[paragraph[i]] += 1
            missing += 1
            i += 1
    return Subarray(start, end)
```

## Explanation
* BLANK

## Code Dissection
1. BLANK