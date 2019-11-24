from test_framework import generic_test


def n_queens(n):
    def dfs(queens, xy_diff, xy_sum):
        row = len(queens)
        if row == n:
            result.append(queens)
        for col in range(n):
            if col not in queens and row - col not in xy_diff and row + col not in xy_sum:
                dfs(queens + [col], xy_diff + [row - col], xy_sum + [row + col])
    result = []
    dfs([], [], [])
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("n_queens.py", 'n_queens.tsv', n_queens,
                                       comp))
