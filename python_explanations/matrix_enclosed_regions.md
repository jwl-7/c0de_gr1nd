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
    keep = [ab for k in range(m + n) for ab in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]
    while keep:
        a, b = keep.pop()
        if 0 <= a < m and 0 <= b < n and board[a][b] == 'W':
            board[a][b] = 'X'
            keep += (a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)
    board[:] = [['B' if char != 'X' else 'W' for char in row] for row in board]
```

## Explanation
* BLANK

## Code Dissection
1. BLANK