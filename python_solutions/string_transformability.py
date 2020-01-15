import collections
import string

from test_framework import generic_test


def transform_string(D, s, t):
    q = collections.deque([(s, 0)])
    visited = set()
    while q:
        word, dist = q.popleft()
        if word == t:
            return dist
        for i in range(len(word)):
            for j in string.ascii_lowercase:
                nxt_word = word[:i] + j + word[i+1:]
                if nxt_word not in visited and nxt_word in D:
                    q.append((nxt_word, dist + 1))
                    visited.add(nxt_word)
    return -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("string_transformability.py",
                                       'string_transformability.tsv',
                                       transform_string))
