from test_framework import generic_test


def is_pattern_contained_in_grid(grid, S):
    def dfs(x, y, idx):
        if idx == len(S):
            return True

        if not (
            0 <= x < len(grid) and
            0 <= y < len(grid[x]) and
            grid[x][y] == S[idx] and
            (x, y, idx) not in visited
        ):
            return False

        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            if dfs(x + dx, y + dy, idx + 1):
                return True

        visited.add((x, y, idx))
        return False

    visited = set()
    return any(
        dfs(i, j, 0)
        for i in range(len(grid))
        for j in range(len(grid[i]))
    )


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_string_in_matrix.py",
                                       'is_string_in_matrix.tsv',
                                       is_pattern_contained_in_grid))
