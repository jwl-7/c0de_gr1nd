from test_framework import generic_test


def ss_decode_col_id(col):
    col_id = 0
    m = 1
    for char in col[::-1]:
        num = ord(char) - 64
        col_id += num * m
        m *= 26
    return col_id


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("spreadsheet_encoding.py",
                                       'spreadsheet_encoding.tsv',
                                       ss_decode_col_id))
