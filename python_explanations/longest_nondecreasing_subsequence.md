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
Let _L_[_i_] = length of longest increasing subsequence of _A_[:_i_+1]
* _L_[_i_] = 1 if _A_[_i_] < previous entries or
* _L_[_i_] = _L_[_j_] + 1 if _A_[_i_] >= _A_[_j_] and _L_[_i_] <= _L_[_j_] =

## Code Dissection
1. Create the DP table
    ```python
    dp = [1] * len(A)
    ```
2. Loop through _A_ and find the longest increasing subsequences of _A_[:_i_+1]
    ```python
    for i in range(len(A)):
        for j in range(i):
            if A[i] >= A[j] and dp[i] <= dp[j]:
                dp[i] = dp[j] + 1
    ```
3. Return the maximum length of the longest nondecreasing subsequence
    ```python
    return max(dp)
    ```