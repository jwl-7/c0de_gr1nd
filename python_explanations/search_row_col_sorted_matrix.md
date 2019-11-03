# Search in a 2D Sorted Array
Given a 2D sorted array _A_ and an integer _x_, return whether or not _x_ is in _A_.

## Examples
|   |_C_<sub>0</sub>|_C_<sub>1</sub>|_C_<sub>2</sub>|_C_<sub>3</sub>|
|---|:---:|:---:|:---:|:---:|
|**_R_<sub>0</sub>**|  1 |  2 |  3 |  4 |
|**_R_<sub>1</sub>**|  5 |  6 |  7 |  8 |
|**_R_<sub>2</sub>**|  9 | 10 | 11 | 12 |
|**_R_<sub>3</sub>**| 13 | 14 | 15 | 16 |

```
 Input: 7
Output: True

 Input: 20
Output: False
```

## Solution
```python
def matrix_search(A, x):
    row = 0
    col = len(A[0]) - 1
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1
        else:
            col -= 1
    return False
```

## Explanation
* If _x_ < _A_[0][_n_-1], then _x_ > elements in row 0
* If _x_ > _A_[0][_n_-1], then _x_ <> elements in col _n_-1

## Code Dissection
1. Start the search from the top-right corner
    ```python
    row = 0
    col = len(A[0]) - 1
    ```
2. Loop until we've searched each column and each row
    ```python
    while row < len(A) and col >= 0:
    ```
3. If there's a match, then return True
    ```python
    if A[row][col] == x:
        return True
    ```
4. Eliminate row from the search
    ```python
    elif A[row][col] < x:
        row += 1
    ```
5. Eliminate col from the search
    ```python
    else:
        col -= 1
    ```
6. If the number doesn't exist, then return False
    ```python
    return False
    ```