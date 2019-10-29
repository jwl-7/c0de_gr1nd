# Compute the _k_ Largest Elements in a Max-Heap
Given a max-heap, represented as an array _A_, design an algorithm that computes the _k_ largest elements stored in the max-heap. You cannot modify the heap.

## Examples
```
 Input: k = 3
        [4, 3, 2, 1, 0]
Output: [4, 3, 2]

 Input: k = 2
        [8, 7, 6, 4, 2, 2, 4, 1, 3]
Output: [8, 7]
```

## Solution
```python
def k_largest_in_binary_heap(A, k):
    max_heap = []
    result = []
    max_heap.append((-A[0], 0))

    for _ in range(k):
        largest_idx = max_heap[0][1]
        result.append(-heapq.heappop(max_heap)[0])

        left = 2 * largest_idx + 1
        if left < len(A):
            heapq.heappush(max_heap, (-A[left], left))

        right = 2 * largest_idx + 2
        if right < len(A):
            heapq.heappush(max_heap, (-A[right], right))
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK