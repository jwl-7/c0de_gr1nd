from test_framework import generic_test


def look_and_say(n):
    s = '1'
    for _ in range(1, n):
        temp = ''
        curr = s[0]
        count = 0
        for char in s:
            if curr == char:
                count += 1
            else:
                temp += str(count) + curr
                curr = char
                count = 1     
        temp += str(count) + char
        s = temp
    return s


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("look_and_say.py", "look_and_say.tsv",
                                       look_and_say))
