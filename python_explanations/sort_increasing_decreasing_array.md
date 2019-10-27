# Sort an Increasing-Decreasing Array
An array is said to be _k_-increasing-decreasing if elements repeteadly increase up to a certain index after which they decrease, then again increase, a total of _k_ times.

Design an efficient algorithm for sorting a *k*-increasing-decreasing array.

## Examples
```
 Input: [1, 2, 3, 2, 1, 4, 5, 10, 9, 4, 4, 1, -1]
Output: [-1, 1, 1, 1, 2, 2, 3, 4, 4, 4, 5, 9, 10]

 Input: [57, 131, 493, 294, 221, 339, 418, 452, 442, 190]
Output: [57, 131, 190, 221, 294, 339, 418, 442, 452, 493]
```

## Solution
```python
def sort_k_increasing_decreasing_array(A):
    sorted_arrays = []
    increasing = True
    start = 0
    for i in range(1, len(A)):
        if A[i] >= A[i-1] and not increasing:
            sorted_arrays.append(A[i-1:start-1:-1])
            increasing = True
            start = i
        elif A[i] < A[i-1] and increasing:
            sorted_arrays.append(A[start:i])
            increasing = False
            start = i
        if i == len(A) - 1:
            if not increasing:
                sorted_arrays.append(A[:start-1:-1])
            else:
                sorted_arrays.append(A[start:])
    return list(heapq.merge(*sorted_arrays))
```

## Explanation
* For an explanation on merging sorted arrays: [Merge Sorted Files](sorted_arrays_merge.md)
* The solution splits the array into a set of increasing arrays and then merges them using a min-heap
* The subarrays are determined by the indexes where the sequence switches from increasing to decreasing or vice versa
* The decreasing sequences are reversed to convert them to increasing ones when putting them into the set of increasing arrays

## Code Dissection
1. Create a list to hold the set of sorted arrays, a boolean to help determine where the sequence changes, and a variable to store where each subsequence starts
    ```python
    sorted_arrays = []
    increasing = True
    start = 0
    ```
2. Loop until the end of the sequence
    ```python
    for i in range(1, len(A)):
    ```
3. If the sequence changes from decreasing -> increasing, append it to *sorted_arrays*
    ```python
    if A[i] >= A[i-1] and not increasing:
        sorted_arrays.append(A[i-1:start-1:-1])
        increasing = True
        start = i
    ```
    * `A[i-1:start-1:-1]` this statement also converts the decreasing subsequence to an increasing one
4. If the sequence changes from increasing -> decreasing, append it to *sorted_arrays*
    ```python
    elif A[i] < A[i-1] and increasing:
        sorted_arrays.append(A[start:i])
        increasing = False
        start = i
    ```
5. When we reach the end of the list, make sure the last subsequence gets appended to *sorted_arrays*
    ```python
    if i == len(A) - 1:
        if not increasing:
            sorted_arrays.append(A[:start-1:-1])
        else:
            sorted_arrays.append(A[start:])
    ```
6. Use `heapq.merge()` to return the merged list of the arrays in *sorted_arrays*
    ```python
    return list(heapq.merge(*sorted_arrays))
    ```