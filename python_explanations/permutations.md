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
    def dfs(options, path):
        if not options:
            result.append(path)
            return
        for i, num in enumerate(options):
            dfs(options[:i] + options[i+1:], path + [num])

    result = []
    dfs(A, [])
    return result
```

## Explanation
* BLANK

## Code Dissection - dfs
1. BLANK

## Code Dissection - permutations
1. Create a list to store the result, run `dfs()`, then return the result
    ```python
    result = []
    dfs(A, [])
    return result
    ```