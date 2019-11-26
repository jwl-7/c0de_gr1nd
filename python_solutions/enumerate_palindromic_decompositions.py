from test_framework import generic_test


def palindrome_decompositions(s):
    def dfs(options, path):
        if not options:
            result.append(path)
            return
        for i in range(1, len(options) + 1):
            if options[:i] == options[:i][::-1]:
                dfs(options[i:], path + [options[:i]])

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
