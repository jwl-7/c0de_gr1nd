# The Pretty Printing Problem
Given a string of space separated words, format the string in accordance with the specified line length, and determine the minimum messiness possible. Words can't be split up across different lines. The messiness of a line that ends with _b_ blank characters = _b_<sup>2</sup>.

## Examples
```
 Input: words = ['a', 'b', 'c', 'd']
        line_length = 5
Output: 8

 Input: words = ['dogs', 'and', 'cars']
        line_length = 15
Output: 4
```

## Solution
```python
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
```

## Explanation
* BLANK

## Code Dissection
1. BLANK