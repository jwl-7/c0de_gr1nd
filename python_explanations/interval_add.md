# Merging Intervals
Given an array of disjointed intervals sorted by the left interval and an additional interval, return the union of the intervals array and the additional given interval.

## Example
```
 Input: [[2, 11], [14, 16], [25, 33], [41, 43], [48, 54]]
        [-4, 20]
Output: [[-4, 20], [25, 33], [41, 43], [48, 54]]
```

## Solution
```python
Interval = collections.namedtuple('Interval', ('left', 'right'))


def add_interval(disjoint_intervals, new_interval):
    i = 0
    n = len(disjoint_intervals)
    merged = []
    while i < n and disjoint_intervals[i].right < new_interval.left:
        merged.append(disjoint_intervals[i])
        i += 1
    while i < n and disjoint_intervals[i].left <= new_interval.right:
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right)
        )
        i += 1
    merged.append(new_interval)
    merged += disjoint_intervals[i:]
    return merged
```

## Explanation
* BLANK

## Code Dissection
1. BLANK