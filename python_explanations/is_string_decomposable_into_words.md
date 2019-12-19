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
    dp = [1] * (dlen + 1)
    for i in range(1, dlen + 1):
        dp[i] = 0
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
1. BLANK