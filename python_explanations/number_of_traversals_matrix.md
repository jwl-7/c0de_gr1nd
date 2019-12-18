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
* BLANK

## Code Dissection
1. BLANK