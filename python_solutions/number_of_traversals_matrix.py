from test_framework import generic_test


def number_of_ways(m, n):
    dp = [1] * n
    for _ in range(1, m):
        for i in range(1, n):
            dp[i] = dp[i-1] + dp[i]
    return dp[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_matrix.py",
                                       'number_of_traversals_matrix.tsv',
                                       number_of_ways))
