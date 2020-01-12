from test_framework import generic_test


def minimum_total_waiting_time(service_times):
    n = len(service_times)
    service_times.sort()
    total_time = 0
    for i, time in enumerate(service_times):
        queries = n - (i + 1)
        total_time += time * queries
    return total_time


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("minimum_waiting_time.py",
                                       'minimum_waiting_time.tsv',
                                       minimum_total_waiting_time))
