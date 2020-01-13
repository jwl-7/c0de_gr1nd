# The 3-Sum Problem
Given an array _A_ of numbers and a target number _t_, determine if there are 3 numbers in _A_ that add up to _t_.

## Examples
```
 Input: A = [2, 3, 5, 7, 11]
        t = 21
Output: True

11 + 7 + 3 = 21


 Input: A = [1, -5, 5, -1, 3, -4]
        t = 12
Output: False
```

## Solution
```python
def has_two_sum(A, t):
    i = 0
    j = len(A) - 1
    while i <= j:
        if A[i] + A[j] == t:
            return True
        elif A[i] + A[j] < t:
            i += 1
        else:
            j -= 1
    return False


def has_three_sum(A, t):
    A.sort()
    return any(has_two_sum(A, t - x) for x in A)
```

## Explanation
* To find 3 numbers _i_, _j_, _k_ that add up to the target _t_:
    * We look for _A_[_i_] + _A_[_j_] + _A_[_k_] = _t_
* This implies that we can also look for _A_[_j_] + _A_[_k_] = _t_ - _A_[_i_]
* Thus, we can use the solution to the 2-Sum problem to solve the 3-sum problem by checking if any number in _A_ can be added to two numbers that add up to _t_

## Code Dissection - has_two_sum
1. Set two pointers at the start and end of the array respectively
    ```python
    i = 0
    j = len(A) - 1
    ```
2. Loop until the two pointers meet each other and search the array
    ```python
    if A[i] + A[j] == t:
        return True
    elif A[i] + A[j] < t:
        i += 1
    else:
        j -= 1
    ```
    * If the 2 numbers < _t_, increment the head pointer _i_
    * If the 2 numbers > _t_, decrement the tail pointer _j_
3. If the search failed, then there are not 2 numbers that add up to the target
    ```python
    return False
    ```

## Code Dissection - has_three_sum
1. Sort the array to avoid having to use additional space
    ```python
    A.sort()
    ```
2. Use `has_two_sum()` to check if any number _x_ in _A_ can be added to two other numbers in _A_ that add up to the target _t_
    ```python
    return any(has_two_sum(A, t - x) for x in A)
    ```
    * This searches for any _A_[_i_] such that _A_[_j_] + _A_[_k_] = _t_ - _A_[_i_]