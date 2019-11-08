# Compute the Union of Intervals
Given a set of intervals, compute their union. The intervals may have open or closed ends.

## Example
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
1. Sort the intervals by the left endpoint and if the endpoints are equal, make sure the one with a closed endpoint comes first
    ```python
    intervals.sort(key=lambda x: (x.left.val, not x.left.is_closed))
    ```
2. Create a result array with the first interval preloaded, since the intervals are now sorted anyways
    ```python
    union = [intervals[0]]
    ```
3. Loop through the intervals and keep track of the previous interval processed, which is the end of the _union_ array
    ```python
    for curr in intervals:
        prev = union[-1]
    ```
4. Check for overlapping intervals:
    1. Check if the current interval's left endpoint overlaps with the previous interval's right endpoint
        ```python
        if (
            curr.left.val < prev.right.val or
            curr.left.val == prev.right.val and
            (curr.left.is_closed or prev.right.is_closed)
        ):
        ```
    2. Check if the previous interval's right endpoint overlaps with the current interval's right endpoint
        ```python
        if (
            curr.right.val > prev.right.val or
            curr.right.val == prev.right.val and
            curr.right.is_closed
        ):
        ```
    3. If we pass the 2 checks, then compute the union of the previous interval and the current interval
        ```python
        union[-1] = Interval(prev.left, curr.right)
        ```
        * Since we modify the last element of the _union_ array, there is nothing to append
5. If the previous and current intervals do not overlap, then append the interval to _union_
    ```python
    else:
        union.append(curr)
    ```
6. Return the union of the set of intervals expressed as a set of disjoint intervals
    ```python
    return union
    ```