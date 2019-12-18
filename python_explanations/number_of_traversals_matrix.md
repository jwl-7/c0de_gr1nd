# Count the Number of Ways to Traverse a 2D Array
Given a 2D array, you are located in the top-left corner. You can only move right or down. Compute the number of paths you can take to get to the bottom-right corner.

## Example
```
 Input: m = 3
        n = 3
Output: 6

There are 6 ways to reach the bottom-right corner:
    1. Right -> Right -> Down -> Down
    2. Right -> Down -> Right -> Down
    3. Right -> Down -> Down -> Right
    4. Down -> Down -> Right -> Right
    5. Down -> Right -> Down -> Right
    6. Down -> Right -> Right -> Down
```

## Solution
```python
def number_of_ways(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for i in range(1, n):
            dp[i] += dp[i-1]
    return dp[-1]
```

## Explanation
* Starting at [1][1] in the grid/DP table, go through each square and record the number of unique paths to that square
* We can ignore the first row and first column since there is only one way to get to those squares
* Unique paths for any square are found by adding the unique paths going in down + unique paths going in right (paths from the squares to its top + its left)
* The bottom-right square in the DP table will contain the total amount of unique paths
* This solution can be optimized by using a 1D array since using a 2D array is redundant

## Code Dissection
1. Create a DP table to store the number of unique paths to each square
    ```python
    dp = [1] * n
    ```
2. Go to each square and record the number of unique paths to that square
    ```python
    for _ in range(1, m):
        for i in range(1, n):
            dp[i] += dp[i-1]
    ```
3. Return the number of unique paths to the bottom-right corner
    ```python
    return dp[-1]
    ```