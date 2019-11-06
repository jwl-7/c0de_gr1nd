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
* For a word of length _n_, search the first _n_ characters of the sentence:
    * If there is not a match, the search continues
    * If there is a match, search the rest of the sentence for the next word

## Code Dissection - match_words
1. Use a counter to store the frequency of word matches in the current search
    ```python
    curr_freq = collections.Counter()
    ```
2. Loop through the sentence from the input start index in steps the size of a word
    ```python
    for i in range(start, start + len(words) * word_len, word_len):
    ```
3. Grab a string the size of a word from the sentence
    ```python
    curr_word = s[i:i+word_len]
    ```
4. If the current string doesn't match any of the words we're searching for, return False
    ```python
    if word_freq[curr_word] == 0:
        return False
    ```
5. If we do find a match, then add it to *curr_freq*
    ```python
    curr_freq[curr_word] += 1
    ```
6. If there are more matches then we're looking for, return False
    ```python
    if curr_freq[curr_word] > word_freq[curr_word]:
        return False
    ```
7. If we found a good match, then return True
    ```python
    return True
    ```

## Code Dissection - find_all_substrings
1. Store the size of a word in a variable for easy usability (the problem assumes all words are the same size)
    ```python
    word_len = len(words[0])
    ```
2. Create a counter for all the words so that we know what to search for
    ```python
    word_freq = collections.Counter(words)
    ```
3. Create an empty array that stores the starting indexes of the substrings we find
    ```python
    result = []
    ```
4. Search the sentence and find the starting indexes of the matching words
    ```python
    for i in range(len(s) - word_len * len(words) + 1):
        if match_words(i):
            result.append(i)
    ```
5. Return the starting indices of the substrings of the sentence that concatenate into all the words
    ```python
    return result
    ```