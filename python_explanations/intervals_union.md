# Compute the Union of Intervals
Given a set of intervals, compute their union. The intervals may have open or closed ends.

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
* We are basically testing for overlaps with the added condition of the open/closed endpoints

There are 2 cases to address:
1. The previous interval in the result and the current interval overlap, in which case compute the union of the two intervals
2. They do not overlap, in which case just add the interval to the result

For overlapping intervals&mdash;Let _x_ = previous interval in the result and _y_ = current interval:
1. _y_.left <= _x_.right
2. If _y_.left == _x_.right, then one of the endpoints must be closed
3. _y_.right >= _x_.right
4. If _y_.right == _x_.right, then _x_'s endpoint must be closed
* All of these conditions must be true before computing the union of two overlapping intervals

## Code Dissection
1. BLANK