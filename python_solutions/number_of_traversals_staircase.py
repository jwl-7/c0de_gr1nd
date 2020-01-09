from test_framework import generic_test


def number_of_ways_to_top(n, k):
    def helper(n, k):
        dp = [1, 1] + [0] * (n - 2)
        for i in range(2, n):
            j = 1
            while j <= k and j <= i:
                dp[i] += dp[i-j]
                j += 1
        return dp[-1]

    return helper(n + 1, k)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("number_of_traversals_staircase.py",
                                       "number_of_traversals_staircase.tsv",
                                       number_of_ways_to_top))
