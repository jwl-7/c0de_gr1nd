from test_framework import generic_test


def examine_buildings_with_sunset(sequence):
    sunset = []
    curr_max = 0
    for i in reversed(range(len(sequence))):
        if sequence[i] > curr_max:
            curr_max = sequence[i]
            sunset.append(i)
    return sunset


def examine_buildings_with_sunset_wrapper(sequence):
    return examine_buildings_with_sunset(iter(sequence))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("sunset_view.py", 'sunset_view.tsv',
                                       examine_buildings_with_sunset))
