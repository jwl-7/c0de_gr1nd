# Delete Duplicates from a Sorted Array
Given a sorted array, remove all the duplicates. Return the number of valid elements after removal. Don't use built-in functions.

## Examples
```
  Input: [-1, -1, 0, 1, 1, 2, 2, 3]
Updated: [-1, 0, 1, 2, 3, 2, 2, 3]
  Valid: [-1, 0, 1, 2, 3]
 Output: 5

  Input: [2, 3, 5, 5, 7, 11, 11, 11, 13]
Updated: [2, 3, 5, 7, 11, 13, 11, 11, 13]
  Valid: [2, 3, 5, 7, 11, 13]
 Output: 6

  Input: [-4, -3, -3, -2, -1, 0, 1, 2, 2, 3, 3, 4, 5, 5]
Updated: [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5, 3, 4, 5, 5]
  Valid: [-4, -3, -2, -1, 0, 1, 2, 3, 4, 5]
 Output: 10
```

## Solution
```python
def delete_duplicates(A):
    idx = 1
    for x in A[1:]:
        if x != A[idx-1]:
            A[idx] = x
            idx += 1
    return idx
```

## Explanation
* Since the array is already sorted, we can use two pointers to iterate through the array and identify duplicates

## Code Dissection
1. Loop through _A_ with 2 pointers
    ```python
    idx = 1
    for x in A[1:]:
    ```
    * _x_ iterates through whole array
    * _idx_ points to tail of answer array
2. If we find a new number, copy it to the tail of the answer array
    ```python
    if x != A[idx-1]:
        A[idx] = x
        idx += 1
    ```
3. Return the length of the answer array (number of valid elements)
    ```python
    return idx
    ```