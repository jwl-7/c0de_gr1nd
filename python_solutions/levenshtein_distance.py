from test_framework import generic_test


def levenshtein_distance(A, B):
    dp = [[i] + [0] * len(B) for i in range(len(A) + 1)]
    dp[0] = [j for j in range(len(B) + 1)]
    for i in range(1, len(A) + 1):
        for j in range(1, len(B) + 1):
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
