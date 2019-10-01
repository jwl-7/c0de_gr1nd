from test_framework import generic_test


def get_valid_ip_address(s):
    ips = []
    for a in range(1, 4):
        for b in range(a + 1, a + 4):
            for c in range(b + 1, b + 4):
                if 0 < len(s) - c < 4:
                    tmp = (s[:a], s[a:b], s[b:c], s[c:])
                    if all(int(x) <= 255 and str(int(x)) == x for x in tmp):
                        ips.append('.'.join(tmp))
    return ips


def comp(a, b):
    return sorted(a) == sorted(b)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "valid_ip_addresses.py",
            'valid_ip_addresses.tsv',
            get_valid_ip_address,
            comparator=comp))
