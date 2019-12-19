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
* BLANK

## Code Dissection
1. BLANK