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
* Recursive formula: _M_(_i_) = min<sub>_j_ <= _i_</sub> _f_(_j_, _i_) + _M_(_j_ - 1)
    * _M_ = minimum messiness
    * _f_(_j_, _i_) = messiness of a line containing words [_j_, _i_]

## Code Dissection
1. Calculate the number of blank spaces left on the first line when including the first word
    ```python
    char_count = line_length - len(words[0])
    ```
2. Create the DP table filled with infinite values and the current messiness for the first line
    ```python
    dp = [char_count**2] + [float('inf')] * (len(words) - 1)
    ```
3. Outer loop: loop through the strings in _words_, calculate the blank spaces left when including _words_[_i_], and store the messiness in the DP table
    ```python
    for i in range(1, len(words)):
        char_count = line_length - len(words[i])
        dp[i] = dp[i-1] + char_count ** 2
    ```
4. Inner loop: Test _words_[_i_-1], _words_[_i_-2], ...
    ```python
    for j in reversed(range(i)):
        char_count -= len(words[j]) + 1
    ```
5. Check if there is enough space to add words
    ```python
    if char_count < 0:
        break
    ```
6. Calculate the messiness when using the _j_ word, and the messiness of the current line
    ```python
    first_j = 0 if j - 1 < 0 else dp[j-1]
    curr_line = char_count ** 2
    ```
7. Compare the current possible messiness to the minimum messiness
    ```python
    dp[i] = min(dp[i], first_j + curr_line)
    ```
8. Return the minimum total messiness
    ```python
    return dp[-1]
    ```