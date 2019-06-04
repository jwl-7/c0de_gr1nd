from test_framework import generic_test


def matrix_in_spiral_order(square_matrix):
    spiral = []
    if square_matrix == []:
        return spiral
    row_start = 0
    col_start = 0
    row_end = len(square_matrix) - 1
    col_end = len(square_matrix[0]) - 1

    while row_start <= row_end and col_start <= col_end:
        spiral.extend([square_matrix[row_start][i] for i in range(col_start, col_end + 1)])
        spiral.extend([square_matrix[i][col_end] for i in range(row_start + 1, row_end + 1)])
        if row_start < row_end:
            spiral.extend([square_matrix[row_end][i] for i in reversed(range(col_start, col_end))])
        if col_start < col_end:
            spiral.extend([square_matrix[i][col_start] for i in reversed(range(row_start + 1, row_end))])
        row_start += 1
        col_start += 1
        row_end -= 1
        col_end -= 1
    return spiral


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spiral_ordering_segments.py",
                                       "spiral_ordering_segments.tsv",
                                       matrix_in_spiral_order))
