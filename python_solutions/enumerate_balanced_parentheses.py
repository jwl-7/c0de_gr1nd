from test_framework import generic_test, test_utils


def generate_balanced_parentheses(num_pairs):
    def dfs(left, right, path):
        if not left and not right:
            result.append(path)
            return
        if left:
            dfs(left - 1, right, path + '(')
        if left < right:
            dfs(left, right - 1, path + ')')

    result = []
    dfs(num_pairs, num_pairs, '')
    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("enumerate_balanced_parentheses.py",
                                       'enumerate_balanced_parentheses.tsv',
                                       generate_balanced_parentheses,
                                       test_utils.unordered_compare))
