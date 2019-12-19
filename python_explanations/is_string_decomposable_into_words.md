# The bedbathandbeyond.&#8203;com Problem
Given a dictionary (list of strings) and a domain (string), check if the domain can be segmented into a sequence of strings in the dictionary. Return the list of segmented strings.

## Examples
```
 Input: dictionary = ['bat', 'car', 'bus']
        domain = 'carbatbus'
Output: ['car', 'bat', 'bus']

 Input: dictionary = ['raw', 'abr', 'bara', 'rawa', 'wr']
        domain = 'rawabawrawr'
Output: []
```

## Solution
```python
def decompose_into_dictionary_words(domain, dictionary):
    dlen = len(domain)
    dp = [1] + [0] * dlen
    for i in range(1, dlen + 1):
        for j in range(i):
            if dp[j] and domain[j:i] in dictionary:
                dp[i] = i - j
                break

    if not dp[-1]:
        return []

    words = []
    idx = dlen
    while idx > 0:
        words.append(domain[idx-dp[idx]:idx])
        idx -= dp[idx]
    return words[::-1]
```

## Explanation
There are two parts to the solution:
1. Check if the domain can be segmented into a sequence of strings in the dictionary
    * Using a DP table, go through the string checking for matches to words in the dictionary
    * If a valid word is found, record the length of the word in the DP table
2. If string can be decomposed, reconstruct the valid sequence found
    * The lengths of the words in the sequence are found at the end of the DP table
    * The sequence can be reconstructed by working backwards in the domain with the word lengths

## Code Dissection
1. Grab the length of _domain_ and create a DP table to keep track of word lengths / valid words
    ```python
    dlen = len(domain)
    dp = [1] + [0] * dlen
    ```
2. Loop through the domain and if we find a valid word that is in the dictionary, add the word's length to the DP table
    ```python
    for i in range(1, dlen + 1):
        for j in range(i):
            if dp[j] and domain[j:i] in dictionary:
                dp[i] = i - j
                break
    ```
3. If we do not find a valid sequence from the domain, then return an empty list
    ```python
    if not dp[-1]:
        return []
    ```
4. If we do find a valid sequence, create a list to store the words and make copy of _dlen_ to help reconstruct the words
    ```python
    words = []
    idx = dlen
    ```
5. Reconstruct the sequence using the word lengths from the DP table
    ```python
    while idx > 0:
        words.append(domain[idx-dp[idx]:idx])
        idx -= dp[idx]
    ```
6. Since we reconstructed the sequence working backwards in _domain_, return the sequence reversed
    ```python
    return words[::-1]
    ```