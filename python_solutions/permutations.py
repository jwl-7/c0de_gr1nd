from test_framework import generic_test, test_utils


def permutations(A):
    def dfs(options, path):
        if not options:
            result.append(path)
            return
        for i, num in enumerate(options):
            dfs(options[:i] + options[i+1:], path + [num])

    result = []
    dfs(A, [])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("permutations.py", 'permutations.tsv',
                                       permutations,
                                       test_utils.unordered_compare))
