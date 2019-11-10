# Find the Closest Entries in Three Sorted Arrays
Given three sorted arrays, compute a value from each array that forms the smallest possible interval.

## Example
```
 Input: [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
 ]
Output: 4
Minimum interval = [3, 4, 7]
Minimum distance = 7 - 3 = 4
```

## Solution
```python
def find_closest_elements_in_sorted_arrays(sorted_arrays):
    diff = float('inf')
    tree = SortedDict()
    for idx, array in enumerate(sorted_arrays):
        i = iter(array)
        nxt = next(i)
        tree[(nxt, idx)] = i
    while True:
        min_val, min_idx = tree.peekitem(0)[0]
        max_val = tree.peekitem()[0][0]
        diff = min(diff, max_val - min_val)
        i = tree.popitem(0)[1]
        nxt = next(i, None)
        if nxt is None:
            return diff
        tree[(nxt, min_idx)] = i
```

## Explanation
* BLANK

## Code Dissection
1. BLANK