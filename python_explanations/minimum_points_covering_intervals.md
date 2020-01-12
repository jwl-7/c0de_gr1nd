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
1. Find the minimal right endpoint
2. Find the first interval not covered by the minimal right endpoint
3. Continue from that interval's right endpoint

## Code Dissection
1. Sort the intervals by the right endpoints
    ```python
    intervals.sort(key=lambda x: x.right)
    ```
2. Initialize the previous right endpoint to -infinity and the total numbers (visits to _intervals_) to zero
    ```python
    prev_right = float('-inf')
    total = 0
    ```
3. Loop through the intervals, starting at the first interval with the minimal right endpoint
    ```python
    for interval in intervals:
    ```
4. Find the first interval not covered by the minimal right endpoint, then continue from that interval's right endpoint
    ```python
    if interval.left > prev_right:
        prev_right = interval.right
        total += 1
    ```
5. Return the minimal set of numbers that covers all the intervals
    ```python
    return total
    ```