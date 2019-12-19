# Pick Up Coins for Maximum Gain
Given a row of an even _n_ coins, you take alternating turns against another player selecting either the first or last coin in the row. Compute the max amount of money that can be won if you have the first turn.

## Examples
```
 Input: [0, 1, 6, 8, 5, 5, 1]
Output: 12

 Input: [3, 5, 6, 6, 1001, 6]
Output: 1010
```

## Solution
```python
def maximum_revenue(coins):
    def max_coin(x, y):
        if x > y:
            return 0

        if dp[x][y] == 0:
            start = coins[x] + min(max_coin(x + 2, y), max_coin(x + 1, y - 1))
            end = coins[y] + min(max_coin(x + 1, y - 1), max_coin(x, y - 2))
            dp[x][y] = max(start, end)
        return dp[x][y]

    dp = [[0] * len(coins) for _ in coins]
    return max_coin(0, len(coins) - 1)
```

## Explanation
If Player A chooses the start of the row of coins (_x_), Player B can choose from [_x_+1, _y_]:
1. If Player B chooses the start (_x_ + 1), recurse for [_x_+2, _y_]
2. If Player B chooses the end (_y_), recurse for [_x_+1, _y_-1]

If Player A chooses the end of the row of coins (_y_), Player B can choose from [_x_, _y_-1]:
1. If Player B chooses the start (_x_, recurse for [_x_+1, _y_-1]
2. If Player B chooses the end (_y_-1), recurse for [_x_, _y_-2]

## Code Dissection - maximum_revenue
1. Create a DP table to store the best choices and return the value from `max_coin()`
    ```python
    dp = [[0] * len(coins) for _ in coins]
    return max_coin(0, len(coins) - 1)
    ```

## Code Dissection - max_coin
1. Base case: there are no coins to choose
    ```python
    if x > y:
        return 0
    ```
2. Check that there are coins to choose
    ```python
    if dp[x][y] == 0:
    ```
3. Case 1: player chooses from the start of the row of coins
    ```python
    start = coins[x] + min(max_coin(x + 2, y), max_coin(x + 1, y - 1))
    ```
4. Case 2: player chooses from the end of the row of coins
    ```python
    end = coins[y] + min(max_coin(x + 1, y - 1), max_coin(x, y - 2))
    ```
5. Compute the optimal choice
    ```python
    dp[x][y] = max(start, end)
    ```
6. Return the optimal choice to the DP table
    ```python
    return dp[x][y]
    ```