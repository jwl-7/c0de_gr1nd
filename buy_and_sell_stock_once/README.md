# Buy and Sell a Stock Once  
  
Problem:  
Write a program that takes an array denoting the daily stock price, and returns the maximum profit that could be made by buying and then selling one share of that stock. There is no need to buy if no profit is possible.   
    
Examples:  
```  
 Input: [0.5, 0.3, 0.5, 0.5, 0.2]	
Output: 0.2	
Conclusion: Buy at 0.3 and sell at 0.5

 Input: [0.3, 0.5, 0.2, 0.5, 0.8, 0.8, 0.1, 0.4]
Output: 0.6	
Conclusion: Buy at 0.2 and sell at 0.8

 Input: [0.8, 1.6, 1.9, 0.5, 0.9, 0.7, 1.7, 0.9, 0.7, 1.6, 2.0, 0.8, 0.5, 0.2, 0.8, 1.7, 0.5, 0.5, 1.0, 0.5]
Output: 1.5	
Conclusion: Buy at 0.2 and sell at 1.7
```  
    
Solution - from [buy-and-sell-stock-once-mysol.py](buy-and-sell-stock-once-mysol.py):  
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
  
Explanation:   
  
1. Create 2 variables to keep track of the minimum price and max profit  
    ```python
    min_price = float('inf')
    max_profit = float('-inf')
    ```  
    -- The initial values are set to inf and -inf so that they will be lower / higher when doing the initial comparison  
2. Loop over each price  
    a. Keep track of the minimum price so far  
    ```python
    min_price = min(min_price, price)
    ```    
    b. Keep track of the max daily profit  
    ```python
    profit = price - min_price
    ```    
    c. Keep track of the max total profit  
    ```python
    max_profit = max(max_profit, profit)
    ```    
6. Return the max profit