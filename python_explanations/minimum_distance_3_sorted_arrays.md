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
Let _s_ be the minimum value and _b_ be the maximum value in a set of 3 numbers:
1. Get the first element from each sorted array&mdash;these are all the minimum values
2. Remove _s_ from the set and replace it with the next element in the array that it belongs to
3. The current distance is (_b_ - _s_)
4. Keep comparing the current distance with the smallest distance so far
5. Return the smallest distance

## Code Dissection
1. BLANK