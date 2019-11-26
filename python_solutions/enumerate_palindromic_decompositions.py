from test_framework import generic_test


def palindrome_decompositions(s):
    def dfs(s, path):
        if not s:
            result.append(path)
            return
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                dfs(s[i:], path + [s[:i]])

    result = []
    dfs(s, [])
    return result


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "enumerate_palindromic_decompositions.py",
            'enumerate_palindromic_decompositions.tsv',
            palindrome_decompositions, comp))
