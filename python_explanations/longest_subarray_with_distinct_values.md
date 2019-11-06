# Find the Longest Subarray with Distinct Entries
Given an array, return the length of the longest subarray with distinct elements.

## Examples
```
 Input: ['a', 'b', 'c', 'd', 'd', 'e', 'f', 'g']
Output: 4

 Input: [1, 1, 2, 3, 4, 5, 5, 6]
Output: 5
```

## Solution
```python
def longest_subarray_with_distinct_entries(A):
    recent = {}
    result = 0
    start = 0
    for i, s in enumerate(A):
        if s not in recent or recent[s] < start:
            result = max(result, i - start + 1)
        else:
            start = recent[s] + 1
        recent[s] = i
    return result
```

## Explanation
* Each distinct element and the index of its most recent occurrence are stored in a hash table
* The start index of the most recent array of distinct elements is updated every time a duplicate element is found

## Code Dissection
1. Create a hash table to store the distinct elements and the indexes of their most recent occurrence
    ```python
    recent = {}
    ```
2. Keep track of the longest subarray found so far and its start index
    ```python
    result = 0
    start = 0
    ```
3. Iterate through the array
    ```python
    for i, s in enumerate(A):
    ```
4. If the current element is not in the table or its most recent occurrence is before the start index of the current subarray, then update the longest subarray found so far
    ```python
    if s not in recent or recent[s] < start:
        result = max(result, i - start + 1)
    ```
5. If the current element is a duplicate, then update the start index &mdash; this is when a new subarray starts
    ```python
    else:
        start = recent[s] + 1
    ```
6. Keep updating the most recent occurrence of each distinct element
    ```python
    recent[s] = i
    ```
7. Return the longest subarray with distinct elements
    ```python
    return result
    ```