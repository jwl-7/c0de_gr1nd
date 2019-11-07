# Remove First-Name Duplicates
Given an array of elements in the form (first-name, last-name), remove all first-name duplicates.

## Example
```
 Input: [['Foo', '1'], ['ABC', '1'], ['Foo', '1']]
Output: [['ABC', '1'], ['Foo', '1']]
```

## Solution
```python
def eliminate_duplicate(A):
    A.sort()
    idx = 1
    for x in A[1:]:
        if x != A[idx-1]:
            A[idx] = x
            idx += 1
    del A[:idx]
```

## Explanation
* For an explanation on removing duplicates from a sorted array: [Delete Duplicates from a Sorted Array](sorted_array_remove_dups.md)
* Despite the fact that we're basically dealing with a 2D array, the solution is the same as removing duplicates from a regular sorted array

## Code Dissection
1. Sort the array first to make it easy to identify duplicates
    ```python
    A.sort()
    ```
2. Loop through _A_ with 2 pointers
    ```python
    idx = 1
    for x in A[1:]:
    ```
    * _x_ iterates through whole array
    * _idx_ points to tail of answer array
3. If we find a new firstname, copy it to the tail of the answer array
    ```python
    if x != A[idx-1]:
        A[idx] = x
        idx += 1
    ```
4. Remove all the duplicates after the tail
    ```python
    del A[:idx]
    ```