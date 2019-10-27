# Compute the Median of Online Data
You want to compute the running median of a sequence of numbers. The sequence is presented to you in a streaming fashion&mdash;you cannot back up to read an earlier value, and you need to output the median after reaching in each new element.

Design an algorithm for computing the running median of a sequence.

## Examples
```
 Input: [1, 2, 3, 4, 5]
Output: [1, 1.5, 2, 2.5, 3]

 Input: [-9, 8, 11, 10, 12, 9, -2, 9, 12, 7, 2, 4]
Output: [-9, -0.5, 8, 9.0, 10, 9.5, 9, 9.0, 9, 9.0, 9, 8.5]
```

## Solution
```python
def online_median(sequence):
    min_heap = []
    max_heap = []
    result = []
    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
        if len(min_heap) < len(max_heap):
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) == len(max_heap):
            result.append((min_heap[0] - max_heap[0]) / 2)
        else:
            result.append(min_heap[0])
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK