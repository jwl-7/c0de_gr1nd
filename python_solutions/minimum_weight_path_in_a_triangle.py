from test_framework import generic_test


def minimum_path_weight(triangle):
    if not triangle:
        return 0
    for i in range(len(triangle) - 2, -1, -1):
        for j in range(len(triangle[i])):
            triangle[i][j] += min(triangle[i+1][j], triangle[i+1][j+1])
    return triangle[0][0]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_weight_path_in_a_triangle.py",
                                       'minimum_weight_path_in_a_triangle.tsv',
                                       minimum_path_weight))
