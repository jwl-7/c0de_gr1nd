# Find the Longest Nondecreasing Subsequence
Given an array of numbers, return the length of the longest increasing subsequence.

## Examples
```
 Input: [1, 1, 5, 2, 5, 3]
Output: 4

 Input: [4, 0, 3, 3, 7, 5, 7]
Output: 5
```

## Solution
```python
def longest_nondecreasing_subsequence_length(A):
    dp = [1] * len(A)
    for i in range(len(A)):
        for j in range(i):
            if A[i] >= A[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
    return max(dp)
```

## Explanation
* BLANK

## Code Dissection
1. BLANK