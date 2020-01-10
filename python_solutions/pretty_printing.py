from test_framework import generic_test


def minimum_messiness(words, line_length):
    char_count = line_length - len(words[0])
    dp = [char_count**2] + [float('inf')] * (len(words) - 1)
    for i in range(1, len(words)):
        char_count = line_length - len(words[i])
        dp[i] = dp[i-1] + char_count ** 2
        for j in reversed(range(i)):
            char_count -= len(words[j]) + 1
            if char_count < 0:
                break
            first_j = 0 if j - 1 < 0 else dp[j-1]
            curr_line = char_count ** 2
            dp[i] = min(dp[i], first_j + curr_line)
    return dp[-1]


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            "pretty_printing.py", 'pretty_printing.tsv', minimum_messiness))
