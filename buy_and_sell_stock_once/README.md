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
    minimum = float('inf')
    max_profit = float('-inf')
    max_profit_today = float('-inf')
    for price in prices:
        minimum = min(minimum, price)
        max_profit_today = price - minimum
        max_profit = max(max_profit, max_profit_today)
    return max_profit
```    
  
Explanation:   
  
1. Create 3 variables to keep track of the minimum price, the max profit that can be made from selling on current day, and the max profit that can be made overall:  
    ```python
    minimum = float('inf')
    max_profit = float('-inf')
    max_profit_today = float('-inf')
    ```  
    -- The initial values are set to inf and -inf so that they will be lower / higher when doing the initial comparison  
2. Loop over each price  
3. Set the minimum price to ```min(minimum, price)```  
4. Set the max daily profit to ```max_profit_today = price - minimum```  
5. Set the max profit overall to ```max_profit = max(max_profit, max_profit_today)```
6. Return the max profit