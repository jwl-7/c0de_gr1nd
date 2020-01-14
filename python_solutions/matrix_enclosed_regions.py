from test_framework import generic_test


def fill_surrounded_regions(board):
    m = len(board)
    n = len(board[0])
    keep = [ab for k in range(m + n) for ab in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]
    while keep:
        a, b = keep.pop()
        if 0 <= a < m and 0 <= b < n and board[a][b] == 'W':
            board[a][b] = 'X'
            keep += (a, b - 1), (a, b + 1), (a - 1, b), (a + 1, b)
    board[:] = [['B' if char != 'X' else 'W' for char in row] for row in board]


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
