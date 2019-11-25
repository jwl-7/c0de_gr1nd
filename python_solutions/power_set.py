from test_framework import generic_test, test_utils


def generate_power_set(S):
    def dfs(options, path):
        result.append(path)
        for i, num in enumerate(options):
            dfs(options[i+1:], path + [num])

    result = []
    dfs(S, [])
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("power_set.py", 'power_set.tsv',
                                       generate_power_set,
                                       test_utils.unordered_compare))
