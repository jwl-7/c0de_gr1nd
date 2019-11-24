# Generate All Nonattacking Placements of _n_-Queens
Given _n_ queens on an _n_ &times; _n_ chessboard, compute all nonattacking placements.

Nonattacking placement = no two queens can threaten each other:
1. Queens can't be in same row
2. Queens can't be in same column
3. Queens can't be in same diagonal

## Example
```
 Input: n = 4
Output: [[1, 3, 0, 2], [2, 0, 3, 1]]
```

| A | B |
|---|---|
|<table><tr><td></td><td>&#9819;</td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>&#9819;</td></tr><tr><td>&#9819;</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td>&#9819;</td><td></td></tr></table>|<table><tr><td></td><td></td><td>&#9819;</td><td></td></tr><tr><td>&#9819;</td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td>&#9819;</td></tr><tr><td></td><td>&#9819;</td><td></td><td></td></tr></table>|

## Solution
```python
def n_queens(n):
    def dfs(queens, xy_diff, xy_sum):
        row = len(queens)
        if row == n:
            result.append(queens)
        for col in range(n):
            if col not in queens and row - col not in xy_diff and row + col not in xy_sum:
                dfs(queens + [col], xy_diff + [row - col], xy_sum + [row + col])
    result = []
    dfs([], [], [])
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK