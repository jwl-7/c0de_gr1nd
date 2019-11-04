from test_framework import generic_test


def find_nearest_repetition(paragraph):
    table = {}
    closest = float('inf')
    for i, s in enumerate(paragraph):
        if s in table:
            distance = i - table[s]
            closest = min(closest, distance)
        table[s] = i
    return closest if closest != float('inf') else -1


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("nearest_repeated_entries.py",
                                       'nearest_repeated_entries.tsv',
                                       find_nearest_repetition))
