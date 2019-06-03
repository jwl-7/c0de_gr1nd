from test_framework import generic_test


def is_valid_list(section):
    section = [x for x in section if x != 0]
    return len(section) == len(set(section))

def is_valid_sudoku(grid):
    for i in range(9):
        if (not is_valid_list(grid[i]) or 
            not is_valid_list([col[i] for col in grid])):
                return False
    for i in range(3):
        for j in range(3):
            if not is_valid_list(grid[a][b]
                                 for b in range(i * 3, 3 * (i + 1)) 
                                 for a in range(j * 3, 3 * (j + 1))):
                return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_valid_sudoku.py",
                                       "is_valid_sudoku.tsv", is_valid_sudoku))
