from test_framework import generic_test


def levenshtein_distance(A, B):
    m, n = len(A), len(B)
    dp = [list(range(n + 1))] + [[i] + [0] * n for i in range(1, m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insert = dp[i][j-1]
            delete = dp[i-1][j]
            replace = dp[i-1][j-1]
            if A[i-1] == B[j-1]:
                dp[i][j] = replace
            else:
                dp[i][j] = min(insert, delete, replace) + 1
    return dp[-1][-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("levenshtein_distance.py",
                                       "levenshtein_distance.tsv",
                                       levenshtein_distance))
