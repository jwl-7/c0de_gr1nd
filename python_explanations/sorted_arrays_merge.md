# Merge Sorted Files
Write a program that takes as input a set of sorted sequences and computes the union of these sequences as a sorted sequence.

## Example
```
 Input: [
     [3, 5, 7],
     [0, 6],
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

# Pythonic Solution
```python
def merge_sorted_arrays_pythonic(sorted_arrays):
    return list(heapq.merge(*sorted_arrays))
```

## Explanation
1. Use a min-heap to store the first element from each array
2. Extract the minimum element in the heap and store it in the result
3. Add the next element from the array that the minimum element belonged to
4. Repeat until all the elements have been processed

## Code Dissection
1. Create a list to use as the min-heap and a list to store the result
    ```python
    min_heap = []
    result = []
    ```
2. Push the first element from each array to the heap
    ```python
    for i in range(len(sorted_arrays)):
        heapq.heappush(min_heap, (sorted_arrays[i][0], i, 0))
    ```
    * The element being pushed is a tuple with 3 items:
        1. array item
        2. array index
        3. item index
3. Create a loop that runs until all the elements have been processed
    ```python
    while min_heap:
    ```
4. Extract the minimum element in the heap and store it in the result
    ```python
    item, arr_idx, item_idx = heapq.heappop(min_heap)
    result.append(item)
    ```
5. Add the next element from the array that the minimum element belonged to
    ```python
    item_idx += 1
    heapq.heappush(min_heap, (sorted_arrays[arr_idx][item_idx], arr_idx, item_idx))
    ```
6. Return the merged list
    ```python
    return result
    ```

## Pythonic Code Dissection
1. Use `heapq.merge()` to return the merged list
    ```python
    return list(heapq.merge(*sorted_arrays))
    ```