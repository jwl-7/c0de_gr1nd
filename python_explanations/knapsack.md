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
* Check each item's weight/value
* If the item's weight < capacity, check if it's optimal to include/exclude the item and add the result to the DP table
* Otherwise ignore the item

## Code Dissection
1. Get the number of items and create the dp table
    ```python
    n = len(items)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    ```
2. Check each item
    ```python
    for i in range(1, n + 1):
        for j in range(1, capacity + 1):
    ```
3. Get the current item weight and value
    ```python
    weight = items[i-1].weight
    value = items[i-1].value
    ```
4. If the item fits in the capacity, check if it's optimal to include/exclude the item
    ```python
    if weight <= j:
        dp[i][j] = max(value + dp[i-1][j-weight], dp[i-1][j])
    else:
        dp[i][j] = dp[i-1][j]
    ```
5. Return the optimum total value of items that fit in the knapsack
    ```python
    return dp[-1][-1]
    ```