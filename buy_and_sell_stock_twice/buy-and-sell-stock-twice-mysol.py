"""Two Phases Algorithm

 Time Complexity: O(n)
Space Complexity: O(n)
"""

class Solution:
    def buy_and_sell_stock_twice(self, prices):
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
    
def main():
    s = Solution()
    test_cases = [
        [0.3, 0.1, 0.4, 0.1],
        [0.2, 0.7, 0.9, 0.4, 0.1, 0.1, 0.5, 0.4, 0.9],
        [0.9, 0.8, 0.8, 0.8, 0.7, 0.2, 1.0, 0.5, 0.6, 1.1, 0.7, 0.3],
        [2.9, 5.1, 5.0, 0.6, 4.2, 1.4, 3.7, 1.9, 4.2, 1.4, 1.9, 1.8, 3.5, 0.6, 0.8, 0.2, 1.2, 1.2, 2.2, 4.5, 0.9, 5.1, 0.6, 1.1, 2.0, 4.5, 1.7, 0.3, 0.2, 2.1, 2.7, 3.6, 2.2, 1.6, 3.0, 3.7, 3.2, 1.4, 2.3, 4.0, 1.9, 3.5, 4.3, 1.3, 0.1, 4.2, 2.4, 1.9, 3.5, 1.1, 0.5],
        [5.5, 8.6, 5.7, 8.4, 1.0, 0.2, 3.0, 3.8, 8.0, 2.5, 7.6, 6.7, 0.6, 5.0, 1.2, 9.4, 4.0, 5.3, 2.9, 2.3, 3.8, 5.2, 5.4, 6.5, 0.5, 7.8, 1.4, 8.6, 7.2, 2.8, 8.8, 0.6, 9.3, 4.1, 6.4, 8.3, 5.1, 5.8, 8.1, 2.8, 0.4, 6.4, 5.5, 6.3, 2.1, 7.3, 8.1, 3.9, 2.2, 2.7, 8.1, 1.1, 3.9, 3.0, 0.2, 7.2, 8.6, 1.6, 2.1, 7.1, 1.7, 7.1, 1.5, 1.0, 4.2, 4.6, 2.0, 3.1, 0.5, 7.8, 5.8, 7.0, 2.1, 1.1, 0.8, 6.6, 7.1, 6.4, 6.6, 2.5, 5.9, 3.8, 8.1, 1.7, 7.3, 3.3, 3.7, 7.3, 7.5, 9.1, 5.4, 4.3, 1.4, 2.6]
        ]
    for prices in test_cases:
        max_profit = s.buy_and_sell_stock_twice(prices)
        print(f'Prices = {prices}')
        print(f'Max Profit = {max_profit}\n')

if __name__ == '__main__':
    main()