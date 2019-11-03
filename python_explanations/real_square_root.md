# Compute the Real Square Root
Given a floating point number _x_, return its square root.

## Examples
```
 Input: 1024.0
Output: 31.999999971129

 Input: 74904312.285
Output: 8654.72774144241
```

## Solution
```python
def square_root(x):
    if x < 1.0:
        left, right = x, 1.0
    else:
        left, right = 1.0, x
    while not math.isclose(left, right):
        mid = (left + right) / 2
        if mid * mid <= x:
            left = mid
        else:
            right = mid
    return left
```

## Explanation
* If _x_ < 1.0, the initial interval is [_x_, 1.0]
* If _x_ >= 1.0, the initial interval is [1.0, _x_]

## Code Dissection
1. Set the left and right pointers such that the inital search interval is [_x_, 1.0] if _x_ < 1.0, else [1.0, _x_]
    ```python
    if x < 1.0:
        left, right = x, 1.0
    else:
        left, right = 1.0, x
    ```
2. Loop until the two pointers meet (may not be exact, since there is float tolerance)
    ```python
    while not math.isclose(left, right):
    ```
    * `math.isclose()` is necessary since we are dealing with floats
3. Compute the mid pointer
    ```python
    mid = (left + right) / 2
    ```
4. Search for the real square root
    ```python
    if mid * mid <= x:
        left = mid
    else:
        right = mid
    ```
5. Return the real square root
    ```python
    return left
    ```