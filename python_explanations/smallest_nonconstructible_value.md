# Smallest Nonconstructible Value
Given an array of positive integers, find the smallest integer that cannot be represented as the sum of any subset of the array.

## Examples
```
 Input: [1, 2, 3, 4]
Output: 11

 Input: [1, 2, 6, 10, 11, 15]
Output: 4
```

## Solution
```python
def smallest_nonconstructible_value(A):
    A.sort()
    x = 1
    for num in A:
        if num <= x:
            x += num
        else:
            break
    return x
```

## Explanation
* The result _x_ is initialized to 1 &mdash; the smallest possible outcome
* If elements from [0 -> _i_ - 1] can represent [1 -> _x_ - 1], then elements from [0 -> _i_] can represent [1 -> _x_ + _A_[_i_] - 1] by adding _A_[_i_] to all subsets that represent [1 -> _x_]

## Code Dissection
1. Make sure the array is sorted
    ```python
    A.sort()
    ```
2. Initialize the result to 1 &mdash; the smallest possible outcome
    ```python
    x = 1
    ```
3. For each number in _A_, if the number <= _x_, add the number to the result
    ```python
    for num in A:
        if num <= x:
            x += num
        else:
            break
    ```
4. Return the smallest nonconstructible value
    ```python
    return x
    ```