# Buy and Sell a Stock Once
Write a program that takes an array denoting the daily stock price, and returns the maximum profit that could be made by buying and then selling one share of that stock. There is no need to buy if no profit is possible.  
  
## Examples
```
 Input: [0.5, 0.3, 0.5, 0.5, 0.2]
Output: 0.2
Conclusion: Buy at 0.3 and sell at 0.5

 Input: [0.3, 0.5, 0.2, 0.5, 0.8, 0.8, 0.1, 0.4]
Output: 0.6
Conclusion: Buy at 0.2 and sell at 0.8

 Input: [0.5, 0.2, 0.2, 1.2, 0.8, 0.6, 1.1, 0.4, 0.1, 1.2, 0.3, 0.5]
Output: 1.1
Conclusion: Buy at 0.1 and sell at 1.2
```
  
## Solution
```python
def buy_and_sell_stock_once(prices):
    min_price = float('inf')
    max_profit = float('-inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit
```
  
## Explanation
* The maximum profit that can be made by selling on a specific day is determined by the minimum of the stock prices over the previous days  
* The solution's algorithm is to iterate over all the stock prices, keeping track of the minimum stock price, and comparing the max daily profit to the max total profit recorded so far  
  
## Code Dissection
1. Create 2 variables that will keep track of the minimum stock price and max total profit  
    ```python
    min_price = float('inf')
    max_profit = float('-inf')
    ```
    * The initial values are set to inf and -inf, so that they will undoubtedly be higher or lower when performing the initial comparison  
2. Loop through all the prices -- take note of the syntax used, it is considered more pythonic  
    ```python
    for price in prices:
    ```
3. Keep track of the minimum stock price so far  
    ```python
    min_price = min(min_price, price)
    ```
4. Keep track of the max daily profit  
    ```python
    profit = price - min_price
    ```
5. Update the max total profit if the max daily profit is higher  
    ```python
    max_profit = max(max_profit, profit)
    ```
6. Return the max total profit  
    ```python
    return max_profit
    ```