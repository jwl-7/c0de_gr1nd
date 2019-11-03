# Buy and Sell a Stock Twice
Given an array whose elements represent the daily stock price, find the maximum profit from buying and selling a share twice. The second buy must occur after the first buy.

## Examples
```
 Input: [0.3, 0.1, 0.4, 0.1]
Output: 0.3
Conclusion: First buy at 0.3 and sell at 0.3, and second buy at 0.1 and sell at 0.4

 Input: [0.2, 0.7, 0.9, 0.4, 0.1, 0.1, 0.5, 0.4, 0.9]
Output: 1.5
Conclusion: First buy at 0.2 and sell at 0.9, and second buy at 0.1 and sell at 0.9

 Input: [0.9, 0.8, 0.8, 0.8, 0.7, 0.2, 1.0, 0.5, 0.6, 1.1, 0.7, 0.3]
Output: 1.4
Conclusion: First buy at 0.2 and sell at 1.0, and second buy at 0.5 and sell at 1.1
```

## Solution
```python
def buy_and_sell_stock_twice(prices):
    profits = []
    min_price = float('inf')
    max_price = float('-inf')
    max_profit = 0.0

    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
        profits.append(max_profit)

    for i, price in reversed(list(enumerate(prices[1:]))):
        max_price = max(max_price, price)
        profit = max_price - price + profits[i]
        max_profit = max(max_profit, profit)
    return max_profit
```

## Explanation
The solution relies on two phases:
1. The forward phase &mdash; used to calculate the max total profit from a single transaction (buy and sell) for each day, and the results are recorded to an array
2. The backward phase &mdash; used to calculate the max total profit from a second transaction for each day, using the array built from the forward phase

## Code Dissection
1. Create an array to hold the first transaction profits, and initialize variables to keep track of the minimum stock price, maximum stock price, and max total profit
    ```python
    profits = []
    min_price = float('inf')
    max_price = float('-inf')
    max_profit = 0.0
    ```
2. Forward phase [left -> right] &mdash; loop over each price
    ```python
    for price in prices:
    ```
    1. Compute the minimum price so far, and the max daily profit
        ```python
        min_price = min(min_price, price)
        profit = price - min_price
        ```
    2. Compute the max total profit by the _i_-th day, and record it in _profits_ &mdash; first transaction
        ```python
        max_profit = max(max_profit, profit)
        profits.append(max_profit)
        ```
3. Backward phase [right -> left] &mdash; loop over each price
    ```python
    for i, price in reversed(list(enumerate(prices[1:]))):
    ```
    * The reason that this statement uses `reversed(list(enumerate))` rather than `enumerate(reversed())` is because the former generates the indexes in reversed order as well as _prices_

    1. Compute the maximum price so far
        ```python
        max_price = max(max_price, price)
        ```
    2. Compute the max daily profit after the _i_-th day &mdash; second transaction, and combine the result with the previous day in _profits_ &mdash; first transaction
        ```python
        profit = max_price - price + profits[i]
        ```
    3. Compute the max total profit of two transactions
        ```python
        max_profit = max(max_profit, profit)
        ```
4. Return the max total profit
    ```python
    return max_profit
    ```