# Find the Nearest Repeated Entries in an Array
Given an array of strings, find the distance between the closest repeated words.

## Examples
```
 Input: ['foo', 'bar', 'asdf', 'foo', 'qwerty', 'qwerty', 'bar']
Output: 1

 Input: ['abc', 'def', 'qrz', 'abc', 'qwerty', 'asdf', 'foo']
Output: 3
```

## Solution
```python
def find_nearest_repetition(paragraph):
    table = {}
    closest = float('inf')
    for i, s in enumerate(paragraph):
        if s in table:
            distance = i - table[s]
            closest = min(closest, distance)
        table[s] = i
    return closest if closest != float('inf') else -1
```

## Explanation
* BLANK

## Code Dissection
1. BLANK