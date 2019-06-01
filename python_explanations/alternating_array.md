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
        if (i % 2 == 0 and A[i] > A[i + 1] or
            i % 2 == 1 and A[i] < A[i + 1]):
            A[i], A[i + 1] = A[i + 1], A[i]
```
  
## Explanation
* [FILL IN]
  
## Code Dissection
1. [FILL IN]