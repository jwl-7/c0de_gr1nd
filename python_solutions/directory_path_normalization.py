from test_framework import generic_test


def shortest_equivalent_path(path):
    stack = []
    for p in path.split('/'):
        if p == '..':
            if not stack or stack[-1] == '..':
                stack.append(p)
            else:
                stack.pop()
        elif p and p != '.':
            stack.append(p)
    return ('/' if path[0] == '/' else '') + '/'.join(stack)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("directory_path_normalization.py",
                                       'directory_path_normalization.tsv',
                                       shortest_equivalent_path))
