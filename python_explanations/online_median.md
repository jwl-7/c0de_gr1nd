# Compute the Median of Online Data
Given a running sequence of numbers, compute the running median after each new element.

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
* A combination of a min-heap and max-heap is used to keep track of the middle two elements and compute the median
* The min-heap stores the smaller half and the max-heap stores the larger half
* The heaps are kept balanced in size

## Code Dissection
1. Create a min-heap, max-heap, and a result list
    ```python
    min_heap = []
    max_heap = []
    result = []
    ```
2. Loop over the sequence, pushing each new element to the min-heap and extracting the smallest element to the max-heap
    ```python
    for x in sequence:
        heapq.heappush(max_heap, -heapq.heappushpop(min_heap, x))
    ```
3. Balance the heaps
    ```python
    if len(min_heap) < len(max_heap):
        heapq.heappush(min_heap, -heapq.heappop(max_heap))
    ```
4. If the min-heap and max-heap are the same size, then extract the top elements from the both heaps and compute the median
    ```python
    if len(min_heap) == len(max_heap):
        result.append((min_heap[0] - max_heap[0]) / 2)
    ```
5. If the heaps are still not balanced, set the top of the min-heap as the median
    ```python
    else:
        result.append(min_heap[0])
    ```
6. Return the running median
    ```python
    return result
    ```