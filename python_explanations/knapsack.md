# The Knapsack Problem
Given a list of items in the form [weight, value] and the max capacity you can carry, find the highest total value you can obtain from the items.

## Example
```
 Input: items = [[10, 5],
                 [20, 10],
                 [30, 15],
                 [40, 20],
                 [50, 25]]
        capacity = 70
Output: 35
```

## Solution
```python
Item = collections.namedtuple('Item', ('weight', 'value'))


def optimum_subject_to_capacity(items, capacity):
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
            weight = items[i-1].weight
            value = items[i-1].value
            if weight <= j:
                dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
            else:
                dp[i][j] = dp[i-1][j]
    return dp[-1][-1]
```

## Explanation
* BLANK

## Code Dissection
1. BLANK