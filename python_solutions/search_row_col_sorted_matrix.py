from test_framework import generic_test


def matrix_search(A, x):
    row = 0
    col = len(A[0]) - 1
    while row < len(A) and col >= 0:
        if A[row][col] == x:
            return True
        elif A[row][col] < x:
            row += 1
        else:
            col -= 1
    return False


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("search_row_col_sorted_matrix.py",
                                       'search_row_col_sorted_matrix.tsv',
                                       matrix_search))
