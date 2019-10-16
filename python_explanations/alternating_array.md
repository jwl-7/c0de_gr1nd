# Computing an Alternation
Write a program that takes an array _A_ of _n_ numbers, and rearranges _A_'s elements to get a new array _B_ having the property that
_B_[0] <= _B_[1] >= _B_[2] <= _B_[3] >= _B_[4] <= _B_[5] >= ...

## Examples
```
Before: [1, 2, 3, 4, 5]
 After: [1, 3, 2, 5, 4]

Before: [4, 2, 1, 1, 7, 9]
 After: [2, 4, 1, 7, 1, 9]
```

## Solution
```python
def rearrange(A):
    for i in range(len(A) - 1):
        if (
            i % 2 == 0 and A[i] > A[i + 1] or
            i % 2 == 1 and A[i] < A[i + 1]
        ):
            A[i], A[i + 1] = A[i + 1], A[i]
```

## Explanation
* The solution follows a simple algorithm, which is to iterate through the array and swapping _A_[_i_] and _A_[_i_ + 1]
for two cases:
    * _i_ is even and _A_[_i_] > _A_[_i_ + 1]
    * _i_ is odd and _A_[_i_] < _A_[_i_ + 1]

## Code Dissection
1. Create a loop that iterates through _A_ - 1, since we will be using _A_[_i_ + 1] and dont want to get an index range error
    ```python
    for i in range(len(A) - 1):
    ```
2. Check for the two cases for which the swap will occur
    ```python
    if (
        i % 2 == 0 and A[i] > A[i + 1] or
        i % 2 == 1 and A[i] < A[i + 1]
    ):
    ```
    * True for even: ```i % 2 == 0```
    * True for odd: ```i % 2 == 1```
3. Swap _A_[_i_] and _A_[_i_ + 1]
    ```python
    A[i], A[i + 1] = A[i + 1], A[i]
    ```