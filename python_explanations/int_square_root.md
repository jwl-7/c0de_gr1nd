# Compute the Integer Square Root
Write a program which takes a nonnegative integer and returns the largest integer whose square is less than or equal to the given integer.

## Examples
```
 Input: 11
Output: 3

 Input: 59
Output: 7
```

## Solution
```python
def square_root(k):
    left = 0
    right = k
    while left <= right:
        mid = (left + right) // 2
        if mid * mid <= k:
            left = mid + 1
        else:
            right = mid - 1
    return left - 1
```

## Explanation
* The initial interval is [0, _k_]
* If _m_<sup>2</sup> <= _k_, all integers <= _m_ have a square <= _k_
    * Update interval to [_m_+1, _R_]
* If _m_<sup>2</sup> > _k_, all integers >= _m_ have a square > _k_
    * Update interval to [_L_, _m_-1]
* The algorithm terminates when the interval is empty, in which case every number < _L_ has a square <= _k_ and _L_'s square is > _k_, so the result is _L_ - 1

## Code Dissection
1. Set a left pointer at 0 and a right pointer at _k_
    ```python
    left = 0
    right = k
    ```
2. Loop until the left and right pointer pass each other
    ```python
    while left <= right:
    ```
3. Compute the mid pointer
    ```python
    mid = (left + right) // 2
    ```
4. Search for the integer square root
    ```python
    if mid * mid <= k:
        left = mid + 1
    else:
        right = mid - 1
    ```
5. Return the integer square root
    ```python
    return left - 1
    ```