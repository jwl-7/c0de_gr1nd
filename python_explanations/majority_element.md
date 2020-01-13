# Find the Majority Element
Given a sequence of strings, find the string that occurs the most within one pass.

## Examples
```
 Input: ['2', '1', '2', '2', '2', '1', '2', '2']
Output: 2

 Input: ['4', '4', '4', '1', '4', '4', '3', '3']
Output: 4
```

## Solution
```python
def majority_search(stream):
    m = None
    m_count = 0
    for s in stream:
        if not m_count:
            m = s
            m_count += 1
        elif m == s:
            m_count += 1
        else:
            m_count -= 1
    return m
```

## Explanation
* BLANK

## Code Dissection
1. BLANK