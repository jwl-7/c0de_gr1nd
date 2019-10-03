from test_framework import generic_test


def rabin_karp(t, s):
    m = len(s)
    n = len(t)
    d = 26
    q = 31
    s_hash = 0
    t_hash = 0
    h = 1

    if n < m:
        return -1

    h = (d ** (m - 1)) % q
    for i in range(m):
        s_hash = (d * s_hash + ord(s[i])) % q
        t_hash = (d * t_hash + ord(t[i])) % q

    for i in range(n - m + 1):
        if s_hash == t_hash and t[i:i+m] == s:
            return i
        if i < n - m:
            t_hash = (d * (t_hash - ord(t[i]) * h) + ord(t[i+m])) % q
    return -1


def rabin_karp_simple(t, s):
    s_hash = hash(s)
    for i in range(len(t) - len(s) + 1):
        t_hash = hash(t[i:i+len(s)])
        if t_hash == s_hash and t[i:i+len(s)] == s:
            return i
    return -1


def boyer_moore_horspool(t, s):
    return t.find(s)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("substring_match.py",
                                       'substring_match.tsv', rabin_karp))
