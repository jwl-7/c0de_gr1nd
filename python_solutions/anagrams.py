import collections

from test_framework import generic_test, test_utils


def find_anagrams(dictionary):
    anagrams = collections.defaultdict(list)
    for s in dictionary:
        anagrams[''.join(sorted(s))].append(s)

    groups = []
    for group in anagrams.values():
        if len(group) >= 2:
            groups.append(group)
    return groups


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "anagrams.py",
            "anagrams.tsv",
            find_anagrams,
            comparator=test_utils.unordered_compare))
