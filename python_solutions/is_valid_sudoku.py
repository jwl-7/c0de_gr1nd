from test_framework import generic_test
from collections import Counter


def is_valid_sudoku(partial_assignment):
    # CHECK COLUMNS
    for i in range(len(partial_assignment)):
        for num, count in Counter([k[i] for k in partial_assignment]).items():
            if num != 0 and count > 1:
                return False

    # CHECK ROWS
    for i in range(len(partial_assignment)):
        for num, count in Counter(partial_assignment[i]).items():
            if num != 0 and count > 1:
                return False
    
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
