# Merging Intervals
Given an array of disjointed intervals sorted by the left interval, merge those intervals with an additional given interval.

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
There are 3 cases that need to be addressed:
1. Disjoint intervals that come before the new interval
2. Disjoint intervals that overlap with the new interval
3. Disjoint intervals that come after the new interval

Let _x_ = disjoint intervals and _y_ = new interval:
1. Before: _x_.right < _y_.left
2. Overlap: _x_.left >= _y_.left and _x_.right <= _y_.right
3. After: _x_.left > _y_.right

## Code Dissection
1. Create a new list to store the merge, an iterator variable, and store the length of the disjoint intervals array
    ```python
    i = 0
    n = len(disjoint_intervals)
    merged = []
    ```
2. Add intervals that come before the new interval to _merged_
    ```python
    while i < n and disjoint_intervals[i].right < new_interval.left:
        merged.append(disjoint_intervals[i])
        i += 1
    ```
3. Find intervals that overlap with the new interval and compute the union before adding it to _merged_
    ```python
    while i < n and disjoint_intervals[i].left <= new_interval.right:
        new_interval = Interval(
            min(new_interval.left, disjoint_intervals[i].left),
            max(new_interval.right, disjoint_intervals[i].right)
        )
        i += 1
    merged.append(new_interval)
    ```
4. Add the intervals that come after the new interval to _merged_
    ```python
    merged += disjoint_intervals[i:]
    ```
5. Return the merged intervals
    ```python
    return merged
    ```