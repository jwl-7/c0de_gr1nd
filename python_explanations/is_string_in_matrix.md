# Search for a Sequence in a 2D Array
Given a 2D array and a sequence of numbers, check if it's possible to traverse the sequence in the grid. The sequence must be traversed using adjacent squares in the correct order.

## Examples
```
2D Array: [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

 Input: S = [1, 2, 5, 8]
Output: True

 Input: S = [1, 2, 3, 5]
Output: False
```

## Solution
```python
def is_pattern_contained_in_grid(grid, S):
    def dfs(x, y, idx):
        if idx == len(S):
            return True

        if not (
            0 <= x < len(grid) and
            0 <= y < len(grid[x]) and
            grid[x][y] == S[idx] and
            (x, y, idx) not in visited
        ):
            return False

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            if dfs(x + dx, y + dy, idx + 1):
                return True

        visited.add((x, y, idx))
        return False

    visited = set()
    return any(
        dfs(i, j, 0)
        for i in range(len(grid))
        for j in range(len(grid[i]))
    )
```

## Explanation
* For some starting point in the matrix (_i_, _j_), search for the first entry in _S_
* If the first entry in _S_ == (_i_, _j_), then check for the remainder of _S_ starting at a point adjacent to the current starting point
* Since recursion is used to search for the remainder of _S_, cache the previously used starting points to avoid unnecessary repeated calls

## Code Dissection
1. BLANK