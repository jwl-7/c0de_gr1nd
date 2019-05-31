from test_framework import generic_test


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


if __name__ == '__main__':
    exit(generic_test.generic_test_main("buy_and_sell_stock_twice.py", "buy_and_sell_stock_twice.tsv", buy_and_sell_stock_twice))