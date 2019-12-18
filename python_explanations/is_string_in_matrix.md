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

## Code Dissection - is_pattern_contained_in_grid
1. Create a cache to store previously used starting points
    ```python
    visited = set()
    ```
    * It is faster to search in a set than an array
2. Check the grid for the sequence starting at (_i_, _j_)
    ```python
    return any(
        dfs(i, j, 0)
        for i in range(len(grid))
        for j in range(len(grid[i]))
    )
    ```

## Code Dissection - dfs
1. If we have reached the end of the sequence, then the search is over
    ```python
    if idx == len(S):
        return True
    ```
2. Check that (_x_, _y_) is in the grid, the current square is the current entry in the sequence, and that we are not at a previously used starting point
    ```python
    if not (
        0 <= x < len(grid) and
        0 <= y < len(grid[x]) and
        grid[x][y] == S[idx] and
        (x, y, idx) not in visited
    ):
        return False
    ```
3. Search for the next entry in one direction recursively
    ```python
    for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
        if dfs(x + dx, y + dy, idx + 1):
            return True
    ```
4. If we can't find the sequence from the starting point, then add it to _visited_ and go back
    ```python
    visited.add((x, y, idx))
    return False
    ```