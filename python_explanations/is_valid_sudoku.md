# The Sudoku Checker Problem
Sudoku is a popular logic-based combinatorial number placement puzzle. The objective is to fill a 9 &times; 9 grid with digits subject to the constraint that each column, each row, and each of the nine 3 &times; 3 sub-grids that compose the grid contains unique integers in [1,9].  

Check whether a 9 &times; 9 2D array representing a partially completed Sudoku is valid. Specifically check that no row, column, or 3 &times; 3 2D subarray contains duplicates. A 0-value in the 2D array indicates that entry is blank; every other entry is in  
[1, 9].  
  
## Examples
```
Input: [[0, 7, 0, 0, 0, 0, 1, 3, 0], 
        [0, 0, 0, 9, 2, 7, 0, 6, 0], 
        [4, 0, 0, 0, 0, 0, 0, 8, 9], 
        [3, 0, 1, 0, 5, 0, 6, 4, 0], 
        [0, 0, 8, 4, 0, 9, 2, 0, 0], 
        [0, 0, 7, 1, 6, 0, 5, 0, 0], 
        [0, 2, 0, 0, 9, 1, 0, 0, 7], 
        [0, 0, 5, 8, 0, 0, 0, 0, 0], 
        [6, 3, 0, 2, 0, 0, 0, 0, 4]]
Output:	True

Input: [[0, 7, 0, 0, 0, 0, 8, 0, 0], 
        [6, 0, 0, 0, 1, 0, 0, 0, 5], 
        [3, 0, 0, 0, 6, 0, 0, 0, 4], 
        [0, 5, 0, 0, 0, 0, 7, 6, 0], 
        [0, 1, 2, 1, 0, 0, 0, 0, 0], 
        [9, 0, 0, 7, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 4, 1], 
        [0, 0, 0, 0, 0, 0, 6, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]	
Output: False
```
  
## Solution
```python
def is_valid_list(section):
    section = [x for x in section if x != 0]
    return len(section) == len(set(section))

def is_valid_sudoku(grid):
    for i in range(9):
        if (not is_valid_list(grid[i]) or 
            not is_valid_list([col[i] for col in grid])):
                return False
    for i in range(3):
        for j in range(3):
            if not is_valid_list(grid[a][b]
                                 for b in range(i * 3, 3 * (i + 1)) 
                                 for a in range(j * 3, 3 * (j + 1))):
                return False
    return True
```
  
## Explanation
Let's look at the layout of a sudoku board:  
```
1 1 1 | 4 4 4 | 7 7 7
1 1 1 | 4 4 4 | 7 7 7
1 1 1 | 4 4 4 | 7 7 7 
---------------------
2 2 2 | 5 5 5 | 8 8 8
2 2 2 | 5 5 5 | 8 8 8
2 2 2 | 5 5 5 | 8 8 8
---------------------
3 3 3 | 6 6 6 | 9 9 9
3 3 3 | 6 6 6 | 9 9 9
3 3 3 | 6 6 6 | 9 9 9
```
* The board has been filled with numbers that represent their sub-grid number  
* The main challenge of the problem is finding out how to grab each column, row, and sub-grid  
* Let's look at extracting each row, column, and sub-grid by hand:  
    ```python
    row1 = grid[0]
    row2 = grid[1]
    row3 = grid[2]
    row4 = grid[3]
    row5 = grid[4]
    row6 = grid[5]
    row7 = grid[6]
    row8 = grid[7]
    row9 = grid[8]

    col1 = [[col[0] for col in grid]]
    col2 = [[col[1] for col in grid]]
    col3 = [[col[2] for col in grid]]
    col4 = [[col[3] for col in grid]]
    col5 = [[col[4] for col in grid]]
    col6 = [[col[5] for col in grid]]
    col7 = [[col[6] for col in grid]]
    col8 = [[col[7] for col in grid]]
    col9 = [[col[8] for col in grid]]

    subgrid1 = [[grid[a][b] for b in range(0, 3)] for a in range(0, 3)]
    subgrid2 = [[grid[a][b] for b in range(0, 3)] for a in range(3, 6)]
    subgrid3 = [[grid[a][b] for b in range(0, 3)] for a in range(6, 9)]
    subgrid4 = [[grid[a][b] for b in range(3, 6)] for a in range(0, 3)]
    subgrid5 = [[grid[a][b] for b in range(3, 6)] for a in range(3, 6)]
    subgrid6 = [[grid[a][b] for b in range(3, 6)] for a in range(6, 9)]
    subgrid7 = [[grid[a][b] for b in range(6, 9)] for a in range(0, 3)]
    subgrid8 = [[grid[a][b] for b in range(6, 9)] for a in range(3, 6)]
    subgrid9 = [[grid[a][b] for b in range(6, 9)] for a in range(6, 9)]
    ```
* When everything is written out, it is a lot easier to derive a statement that can grab each and understand the code in the solution:  
```python
rows = [grid[i] for i in range(9)]
cols = [[col[i] for col in grid] for i in range(9)]
subgrids = ([grid[a][b] 
             for b in range(i * 3, 3 * (i + 1)) 
             for a in range(j * 3, 3 * (j + 1))
        ]    for i in range(3) for j in range(3)) 
```
  
## Code Dissection - is_valid_list
1. Filter out the zeroes from the list, since for this problem, they represent blank entries  
    ```python
    section = [x for x in section if x != 0]
    ```
    * This type of expression is referred to as list comprehension  
2. Return a boolean of whether or not the filtered list contains any duplicates  
    ```python
    return len(section) == len(set(section))
    ```
    * ```len(set(x))``` tells us the size of unique elements in x  
    * This statement is comparing the size of the filtered list to the size of unique elements, and if they are not equal, then the list contains duplicates  
  
## Code Dissection - is_valid_sudoku
1. Loop over each column and grid to check for duplicates  
    ```python
    for i in range(9):
        if (not is_valid_list(grid[i]) or 
            not is_valid_list([col[i] for col in grid])):
                return False
    ```
    * ```if not x``` in Python is the Pythonic way of saying ```if x == False```  
2. Loop over each sub-grid and check for duplicates  
    ```python
    for i in range(3):
        for j in range(3):
            if not is_valid_list(grid[a][b]
                                 for b in range(i * 3, 3 * (i + 1)) 
                                 for a in range(j * 3, 3 * (j + 1))):
                return False
    ```
3. If there are no duplicates in each row, column, and sub-grid, then the sudoku grid is valid  
    ```python
    return True
    ```