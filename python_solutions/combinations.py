from test_framework import generic_test, test_utils


def combinations(n, k):
    def dfs(options, k, path):
        if not k:
            result.append(path)
            return
        for i, num in enumerate(options):
            dfs(options[i+1:], k - 1, path + [num])

    result = []
    dfs(range(1, n + 1), k, [])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "combinations.py",
            'combinations.tsv',
            combinations,
            comparator=test_utils.unordered_compare))
