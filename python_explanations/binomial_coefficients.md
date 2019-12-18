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
* Factorial formula: C(_n_, _k_) = _n_! / _k_!(_n_ - _k_)! for 0 <= _k_ <= _n_
* Recursive formula: C(_n_, _k_) = C(_n_ - 1, _k_ - 1) + C(_n_ - 1, _k_)
* The solution is optimized by using the concept of Pascal's triangle to compute the product

## Code Dissection
1. Use the symmetry rule for binomial coefficients to define _k_
    ```python
    k = min(k, n - k)
    ```
2. Create a DP table the size of _k_
    ```python
    dp = [1] + [0] * k
    ```
3. Loop _n_ times
    ```python
    for i in range(1, n + 1):
    ```
4. Compute the next row of Pascal's triangle using the previous row
    ```python
    j = min(i, k)
    while j > 0:
        dp[j] += dp[j-1]
        j -= 1
    ```
5. Return the binomial coefficient (last computed row)
    ```python
    return dp[-1]
    ```