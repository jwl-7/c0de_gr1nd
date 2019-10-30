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
* Since we are not supposed to modify the heap, the solution is to create another max-heap and extract the _k_ largest elements from the original heap
* The index of a left child node = 2_i_ + 1
* The index of a right child node = 2_i_ + 2

## Code Dissection
1. Create a new max-heap and a list to store the result
    ```python
    max_heap = []
    result = []
    ```
2. Add the largest element from _A_ to our new max-heap
    ```python
    max_heap.append((-A[0], 0))
    ```
    * The element is a tuple in the form of (value, index)
3. Loop through *k* elements
    ```python
    for _ in range(k):
    ```
4. Find the index of the largest element in the max-heap
    ```python
    largest_idx = max_heap[0][1]
    ```
5. Add the largest element in the max-heap to _result_
    ```python
    result.append(-heapq.heappop(max_heap)[0])
    ```
6. Get the left child's index of the largest element in the max-heap; if it exists, push it to the max-heap
    ```python
    left = 2 * largest_idx + 1
    if left < len(A):
        heapq.heappush(max_heap, (-A[left], left))
    ```
7. Get the right child's index of the largest element in the max-heap; if it exists, push it to the max-heap
    ```python
    right = 2 * largest_idx + 2
    if right < len(A):
        heapq.heappush(max_heap, (-A[right], right))
    ```
8. Return the _k_ largest elements
    ```python
    return result
    ```