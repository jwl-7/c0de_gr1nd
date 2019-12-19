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
* BLANK

## Code Dissection
1. BLANK