from test_framework import generic_test


def majority_search(stream):
    m = None
    m_count = 0
    for s in stream:
        if not m_count:
            m = s
            m_count += 1
        elif m == s:
            m_count += 1
        else:
            m_count -= 1
    return m


def majority_search_wrapper(stream):
    return majority_search(iter(stream))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("majority_element.py",
                                       'majority_element.tsv',
                                       majority_search_wrapper))
