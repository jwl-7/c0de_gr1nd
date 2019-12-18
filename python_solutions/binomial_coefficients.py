from test_framework import generic_test


def compute_binomial_coefficient(n, k):
    k = min(k, n - k)
    dp = [1] + [0] * k
    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            dp[j] += dp[j-1]
            j -= 1
    return dp[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("binomial_coefficients.py",
                                       'binomial_coefficients.tsv',
                                       compute_binomial_coefficient))
