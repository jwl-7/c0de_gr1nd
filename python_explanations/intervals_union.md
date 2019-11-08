# Compute the Union of Intervals
Given a set of intervals, compute their union.

## Examples
```
False = open end
 True = closed end

 Input: [[1, false, 3, true], [22, true, 31, true], [29, true, 30, true]]
Output: [[1, false, 3, true], [22, true, 31, true]]
```

## Solution
```python
Endpoint = collections.namedtuple('Endpoint', ('is_closed', 'val'))
Interval = collections.namedtuple('Interval', ('left', 'right'))


def union_of_intervals(intervals):
    intervals.sort(key=lambda x: (x.left.val, not x.left.is_closed))
    union = [intervals[0]]
    for curr in intervals:
        prev = union[-1]
        if (
            curr.left.val < prev.right.val or
            curr.left.val == prev.right.val and
            (curr.left.is_closed or prev.right.is_closed)
        ):
            if (
                curr.right.val > prev.right.val or
                curr.right.val == prev.right.val and
                curr.right.is_closed
            ):
                union[-1] = Interval(prev.left, curr.right)
        else:
            union.append(curr)
    return union
```

## Explanation
* BLANK

## Code Dissection
1. BLANK