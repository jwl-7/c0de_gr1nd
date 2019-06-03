from test_framework import generic_test
from collections import Counter


def is_valid_sudoku(partial_assignment):
    for i in range(9):
        for num, count in Counter(partial_assignment[i]).items():
            if num != 0 and count > 1:
                return False
    for i in range(9):
        for num, count in Counter([k[i] for k in partial_assignment]).items():
            if num != 0 and count > 1:
                return False
    for i in range(3): 
        for j in range(3):
            for num, count in Counter([
                    partial_assignment[a][b] 
                    for b in range(i * 3, 3 * (i + 1)) 
                    for a in range(j * 3, 3 * (j + 1))
                ]).items():
                if num != 0 and count > 1:
                    return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
