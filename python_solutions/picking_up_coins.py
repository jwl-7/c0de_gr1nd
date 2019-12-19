from test_framework import generic_test


def maximum_revenue(coins):
    def max_coin(x, y):
        if x > y:
            return 0

        if dp[x][y] == 0:
            start = coins[x] + min(max_coin(x + 2, y), max_coin(x + 1, y - 1))
            end = coins[y] + min(max_coin(x + 1, y - 1), max_coin(x, y - 2))
            dp[x][y] = max(start, end)
        return dp[x][y]

    dp = [[0] * len(coins) for _ in coins]
    return max_coin(0, len(coins) - 1)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "picking_up_coins.py", 'picking_up_coins.tsv', maximum_revenue))
