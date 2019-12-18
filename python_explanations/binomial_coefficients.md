# Compute the Binomial Coefficients
Calculate _n_ choose _k_ (C(_n_, _k_)) that does not overflow when the result fits in a 32-bit integer.

## Examples
```
 Input: n = 7
        k = 2
Output: 21

 Input: n = 12
        k = 3
Output: 220
```

## Solution
```python
def compute_binomial_coefficient(n, k):
    k = min(k, n - k)
    dp = [1] + [0] * k
    for i in range(1, n + 1):
        j = min(i, k)
        while j > 0:
            dp[j] += dp[j-1]
            j -= 1
    return dp[-1]
```

## Explanation
* BLANK

## Code Dissection
1. BLANK