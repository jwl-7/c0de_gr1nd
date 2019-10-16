# Rotate a 2D Array
Write a function that takes as input an _n_ &times; _n_ 2D array, and rotates the array by 90 degrees clockwise.

## Examples
* Let _C_ and _R_ represent column and row ids

##### 4 &times; 4 array
|   |_C_<sub>0</sub>|_C_<sub>1</sub>|_C_<sub>2</sub>|_C_<sub>3</sub>|
|---|:---:|:---:|:---:|:---:|
|**_R_<sub>0</sub>**|  1 |  2 |  3 |  4 |
|**_R_<sub>1</sub>**|  5 |  6 |  7 |  8 |
|**_R_<sub>2</sub>**|  9 | 10 | 11 | 12 |
|**_R_<sub>3</sub>**| 13 | 14 | 15 | 16 |

##### 4 &times; 4 array rotated 90 degrees clockwise
|   |_C_<sub>0</sub>|_C_<sub>1</sub>|_C_<sub>2</sub>|_C_<sub>3</sub>|
|---|:---:|:---:|:---:|:---:|
|**_R_<sub>0</sub>**| 13 |  9 |  5 |  1 |
|**_R_<sub>1</sub>**| 14 | 10 |  6 |  2 |
|**_R_<sub>2</sub>**| 15 | 11 |  7 |  3 |
|**_R_<sub>3</sub>**| 16 | 12 |  8 |  4 |

## Solution
```python
def rotate_matrix(square_matrix):
    square_matrix[:] = [[row[i] for row in square_matrix[::-1]] for i in range(len(square_matrix))]
```

## Explanation
While the solution is little bit of code golf, it relies on 2 basic steps:
1. Find the transpose of the matrix -- this is the matrix flipped over its diagonal
2. Reverse each row in the transpose

## Code Dissection
1. Find the transpose of the matrix and reverse each row in the transpose
    ```python
    square_matrix[:] = [[row[i] for row in square_matrix[::-1]] for i in range(len(square_matrix))]
    ```
    Let's break down some of the list comprehension involved here:
    * This statement would create a matrix _x_ that is the exact same as the original matrix
        ```python
        x = [square_matrix[i] for i in range(len(square_matrix))]
        ```
    * This statement would also create a matrix _x_ that is the exact same as the original matrix
        ```python
        x = [row for row in square_matrix]
        ```
    * So this statement sets each row _i_ to each column _i_
        ```python
        [[row[i] for row in square_matrix] for i in range(len(square_matrix))]
        ```
    * `[::-1]` reverses a list
    * Thus, the solution sets each row _i_ to the reverse of each column _i_

## Step-by-Step Example
* Let _C_ and _R_ represent column and row ids

##### 3 &times; 3 array
|   |_C_<sub>0</sub>|_C_<sub>1</sub>|_C_<sub>2</sub>|
|---|:---:|:---:|:---:|
|**_R_<sub>0</sub>**| 1 | 2 | 3 |
|**_R_<sub>1</sub>**| 4 | 5 | 6 |
|**_R_<sub>2</sub>**| 7 | 8 | 9 |

##### 3 &times; 3 array transposed
|   |_C_<sub>0</sub>|_C_<sub>1</sub>|_C_<sub>2</sub>|
|---|:---:|:---:|:---:|
|**_R_<sub>0</sub>**| 1 | 4 | 7 |
|**_R_<sub>1</sub>**| 2 | 5 | 8 |
|**_R_<sub>2</sub>**| 3 | 6 | 9 |

##### 3 &times; 3 array rotated 90 degrees clockwise
|   |_C_<sub>0</sub>|_C_<sub>1</sub>|_C_<sub>2</sub>|
|---|:---:|:---:|:---:|
|**_R_<sub>0</sub>**| 7 | 4 | 1 |
|**_R_<sub>1</sub>**| 8 | 5 | 2 |
|**_R_<sub>2</sub>**| 9 | 6 | 4 |