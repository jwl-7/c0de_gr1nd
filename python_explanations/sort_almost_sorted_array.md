# Sort an Almost-Sorted Array
Write a program which takes as input a very long sequence of numbers and prints the numbers in sorted order. Each number is at most _k_ away from its correctly sorted position.

## Examples
```
 Input: [1, 2, 0, 3]
        k = 4
Output: [0, 1, 2, 3]

 Input: [-5, -3, -2, -5, 3]
        k = 5
Output: [-5, -5, -3, -2, 3]
```

## Solution
```python
def sort_approximately_sorted_array(sequence, k):
    min_heap = []
    result = []
    for i in itertools.islice(sequence, k):
        heapq.heappush(min_heap, i)
    for i in sequence:
        result.append(heapq.heappushpop(min_heap, i))
    while min_heap:
        result.append(heapq.heappop(min_heap))
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK