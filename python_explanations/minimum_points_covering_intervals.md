# The Interval Covering Problem
Given a set of closed intervals, find the minimum sized set of numbers that covers the intervals.

## Examples
```
 Input: [[1, 5], [2, 3], [3, 4]]
Output: 1

 Input: [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
Output: 3
```

## Solution
```python
Interval = collections.namedtuple('Interval', ('left', 'right'))


def find_minimum_visits(intervals):
    intervals.sort(key=lambda x: x.right)
    prev_right = float('-inf')
    total = 0
    for interval in intervals:
        if interval.left > prev_right:
            prev_right = interval.right
            total += 1
    return total
```

## Explanation
* BLANK

## Code Dissection
1. BLANK