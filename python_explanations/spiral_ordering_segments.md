# Compute the Spiral Ordering of a 2D Array
Write a program which takes an _n_ &times; _n_ 2D array and returns the spiral ordering of the array.  
  
## Examples
* Let _C_ and _R_ represent column and row ids  
  
##### 3 &times; 3 array
|   |_C_<sub>0</sub>|_C_<sub>1</sub>|_C_<sub>2</sub>|
|---|:---:|:---:|:---:|
|**_R_<sub>0</sub>**| 1 | 2 | 3 |
|**_R_<sub>1</sub>**| 4 | 5 | 6 |
|**_R_<sub>2</sub>**| 7 | 8 | 9 |

a. The spiral ordering for this array is [1, 2, 3, 6, 9, 8, 7, 4, 5]  
  
##### 4 &times; 4 array
|   |_C_<sub>0</sub>|_C_<sub>1</sub>|_C_<sub>2</sub>|_C_<sub>3</sub>|
|---|:---:|:---:|:---:|:---:|
|**_R_<sub>0</sub>**|  1 |  2 |  3 |  4 |
|**_R_<sub>1</sub>**|  5 |  6 |  7 |  8 |
|**_R_<sub>2</sub>**|  9 | 10 | 11 | 12 |
|**_R_<sub>3</sub>**| 13 | 14 | 15 | 16 |

b. The spiral ordering for this array is [1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10]
  
## Solution
```python
def matrix_in_spiral_order(square_matrix):
    spiral = []
    if square_matrix == []:
        return spiral
    row_start = 0
    col_start = 0
    row_end = len(square_matrix) - 1
    col_end = len(square_matrix[0]) - 1

    while row_start <= row_end and col_start <= col_end:
        spiral.extend([square_matrix[row_start][i] for i in range(col_start, col_end + 1)])
        spiral.extend([square_matrix[i][col_end] for i in range(row_start + 1, row_end + 1)])
        if row_start < row_end:
            spiral.extend([square_matrix[row_end][i] for i in reversed(range(col_start, col_end))])
        if col_start < col_end:
            spiral.extend([square_matrix[i][col_start] for i in reversed(range(row_start + 1, row_end))])
        row_start += 1
        col_start += 1
        row_end -= 1
        col_end -= 1
    return spiral
```
  
## Explanation
The solution uses the following steps in a loop:  
1. Extract the first _n_ - 1 elements of the first row  
2. Extract the first _n_ - 1 elements of the last column  
3. Extract the last _n_ - 1 elements of the last row in reverse order  
4. Extract the last _n_ - 1 elements of the first column in reverse order  
5. Loop for remaining rows and columns  
  
## Code Dissection
1. BLANK  