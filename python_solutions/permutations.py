from test_framework import generic_test, test_utils


def permutations(A):
    def dfs(A, path):
        if not A:
            result.append(path)
        for i in range(len(A)):
            dfs(A[:i] + A[i+1:], path + [A[i]])

    result = []
    dfs(A, [])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
