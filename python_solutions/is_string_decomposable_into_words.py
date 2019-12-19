import functools

from test_framework import generic_test
from test_framework.test_failure import TestFailure
from test_framework.test_utils import enable_executor_hook


def decompose_into_dictionary_words(domain, dictionary):
    dlen = len(domain)
    dp = [1] * (dlen + 1)
    for i in range(1, dlen + 1):
        dp[i] = 0
        for j in range(i):
            if dp[j] and domain[j:i] in dictionary:
                dp[i] = i - j
                break

    if not dp[-1]:
        return []

    words = []
    idx = dlen
    while idx > 0:
        words.append(domain[idx-dp[idx]:idx])
        idx -= dp[idx]
    return words[::-1]


@enable_executor_hook
def decompose_into_dictionary_words_wrapper(executor, domain, dictionary,
                                            decomposable):
    result = executor.run(
        functools.partial(decompose_into_dictionary_words, domain, dictionary))

    if not decomposable:
        if result:
            raise TestFailure('domain is not decomposable')
        return

    if any(s not in dictionary for s in result):
        raise TestFailure('Result uses words not in dictionary')

    if ''.join(result) != domain:
        raise TestFailure('Result is not composed into domain')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "is_string_decomposable_into_words.py",
            'is_string_decomposable_into_words.tsv',
            decompose_into_dictionary_words_wrapper))
