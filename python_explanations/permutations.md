# Generate Permutations
Given an array of distinct integers, generate all permutations of the array.

## Example
```
 Input: [0, 1, 2]
Output: [[0, 1, 2], [0, 2, 1], [1, 0, 2], [1, 2, 0], [2, 0, 1], [2, 1, 0]]
```

## Solution
```python
def permutations(A):
    def dfs(A, path):
        if not A:
            result.append(path)
        for i in range(len(A)):
            dfs(A[:i] + A[i+1:], path + [A[i]])

    result = []
    dfs(A, [])
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK