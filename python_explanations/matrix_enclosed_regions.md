# Compute Enclosed Regions
Given a 2D array filled with 'W's and 'B's, replace every 'W' in an enclosed region with a 'B'. A 'W' is in an enclosed region if there is no path along adjacent 'W's to a boundary of the matrix.

## Example
```
 Input: [['B', 'B', 'B', 'B'],
         ['B', 'W', 'W', 'B'],
         ['B', 'W', 'W', 'B'],
         ['W', 'B', 'B', 'B'],
         ['B', 'B', 'W', 'B']]

Output: [['B', 'B', 'B', 'B'],
         ['B', 'B', 'B', 'B'],
         ['B', 'B', 'B', 'B'],
         ['W', 'B', 'B', 'B'],
         ['B', 'B', 'W', 'B']]
```

## Solution
```python
def fill_surrounded_regions(board):
    m = len(board)
    n = len(board[0])
    boundary = [xy for k in range(m + n) for xy in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]
    while boundary:
        x, y = boundary.pop()
        if 0 <= x < m and 0 <= y < n and board[x][y] == 'W':
            board[x][y] = 'X'
            boundary += (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)
    board[:] = [['B' if char != 'X' else 'W' for char in row] for row in board]
```

## Explanation
* Find every 'W' on the boundary and change its region's cells to 'X'
* Replace every 'W' remaining (those enclosed) with 'B'
* Change every 'X' back to a 'W'

## Code Dissection
1. Compute the width and height of the board
    ```python
    m = len(board)
    n = len(board[0])
    ```
2. Using the board's dimensions, compute the coordinates of the cells on the boundary
    ```python
    boundary = [xy for k in range(m + n) for xy in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]
    ```
3. Check the boundary cells to find any 'W's
    ```python
    while boundary:
        x, y = boundary.pop()
        if 0 <= x < m and 0 <= y < n and board[x][y] == 'W':
    ```
4. Replace every 'W' on the boundary with 'X', then add its adjacent cells to _boundary_
    ```python
    board[x][y] = 'X'
    boundary += (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)
    ```
5. Replace every remaining (enclosed) 'W' with 'B', then change every 'X' back to a 'W'
    ```python
    board[:] = [['B' if char != 'X' else 'W' for char in row] for row in board]
    ```