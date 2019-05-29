# Buy and Sell a Stock Twice    
  
Problem:  
Write a program that computes the maximum profit that can be made by buying and selling a share at most twice. The second buy must be made on another date after the first sale.   
    
Examples:  
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
    
Solution - from [buy-and-sell-stock-twice-mysol.py](buy-and-sell-stock-twice-mysol.py):  
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
        profit = max_price - price
        max_profit = max(max_profit, profit + profits[i])
    return max_profit
```    
  
Explanation:   
  
