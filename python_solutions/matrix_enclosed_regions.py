from test_framework import generic_test


def fill_surrounded_regions(board):
    m = len(board)
    n = len(board[0])
    boundary = [xy for k in range(m + n) for xy in ((0, k), (m - 1, k), (k, 0), (k, n - 1))]
    while boundary:
        x, y = boundary.pop()
        if 0 <= x < m and 0 <= y < n and board[x][y] == 'W':
            board[x][y] = 'X'
            boundary += (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y)
    board[:] = [['B' if char != 'X' else 'W' for char in row] for row in board]


def fill_surrounded_regions_wrapper(board):
    fill_surrounded_regions(board)
    return board


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("matrix_enclosed_regions.py",
                                       'matrix_enclosed_regions.tsv',
                                       fill_surrounded_regions_wrapper))
