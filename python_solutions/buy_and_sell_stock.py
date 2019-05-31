from test_framework import generic_test


def buy_and_sell_stock_once(prices):
    min_price = float('inf')
    max_profit = float('-inf')
    for price in prices:
        min_price = min(min_price, price)
        profit = price - min_price
        max_profit = max(max_profit, profit)
    return max_profit


if __name__ == '__main__':
    exit(generic_test.generic_test_main("buy_and_sell_stock.py", "buy_and_sell_stock.tsv", buy_and_sell_stock_once))