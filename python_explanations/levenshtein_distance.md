# Compute the Levenshtein Distance
Given two strings _A_ and _B_, find the minimum number of edits needed to convert _A_ to _B_.

## Examples
```
 Input: A = 'racecar'
        B = 'honda'
Output: 6

 Input: A = 'kitten'
        B = 'sitting'
Output: 3
```

## Solution
```python
def levenshtein_distance(A, B):
    m, n = len(A), len(B)
    dp = [[i] + [0] * n for i in range(m + 1)]
    dp[0] = [j for j in range(n + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            insert = dp[i][j-1]
            delete = dp[i-1][j]
            replace = dp[i-1][j-1]
            if A[i-1] == B[j-1]:
                dp[i][j] = replace
            else:
                dp[i][j] = min(insert, delete, replace) + 1
    return dp[-1][-1]
```

## Explanation
There are 3 operations to perform on a string to convert it:
1. Insert character
2. Delete character
3. Replace character



## Code Dissection
1. BLANK