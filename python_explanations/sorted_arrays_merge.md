# Merge Sorted Files
Write a program that takes as input a set of sorted sequences and computes the union of these sequences as a sorted sequence.

## Examples
```
 Input: [
     [3, 5, 7]
     [0, 6]
     [0, 6, 28]
 ]
Output: [0, 0, 3, 5, 6, 6, 7, 28]
```

## Solution
```python
def merge_sorted_arrays(sorted_arrays):
    min_heap = []
    result = []
    for i in range(len(sorted_arrays)):
        heapq.heappush(min_heap, (sorted_arrays[i][0], i, 0))
    while min_heap:
        item, arr_idx, item_idx = heapq.heappop(min_heap)
        result.append(item)
        if item_idx + 1 < len(sorted_arrays[arr_idx]):
            item_idx += 1
            heapq.heappush(min_heap, (sorted_arrays[arr_idx][item_idx], arr_idx, item_idx))
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK