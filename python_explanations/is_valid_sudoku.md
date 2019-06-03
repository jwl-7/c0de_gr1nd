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
def is_valid_sudoku(partial_assignment):
    # TODO - you fill in here.
    return True
```
  
## Explanation
* BLANK  
  
## Code Dissection
1. BLANK  