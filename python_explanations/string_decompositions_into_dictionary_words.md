# Compute All String Decompositions
Given a sentence string and an array of words, find the starting indices of substrings that concatenate into each word.

## Examples
```
 Input:     s = 'abcbanabanabc'
        words = ['aba', 'nab']
Output: [6]

 Input:     s = 'barfoobardograb'
        words = ['foo', 'bar']
Output: [0, 3]
```

## Solution
```python
def find_all_substrings(s, words):
    def match_words(start):
        curr_freq = collections.Counter()
        for i in range(start, start + len(words) * word_len, word_len):
            curr_word = s[i:i+word_len]
            if word_freq[curr_word] == 0:
                return False
            curr_freq[curr_word] += 1
            if curr_freq[curr_word] > word_freq[curr_word]:
                return False
        return True

    word_len = len(words[0])
    word_freq = collections.Counter(words)
    result = []
    for i in range(len(s) - word_len * len(words) + 1):
        if match_words(i):
            result.append(i)
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK