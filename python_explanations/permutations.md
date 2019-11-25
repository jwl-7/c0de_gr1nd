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
* In `dfs()`, the path so far is built using numbers from the `options` parameter, and once the path has used up all those numbers, the path is added to the result
* For example, if _A_ = [1, 2, 3], and the first part of the path is [1], then the options for the second part of the path will be 2 or 3

## Code Dissection - dfs
1. If we run out of options (numbers), then the path is built, so add it to the result
    ```python
    if not options:
        result.append(path)
        return
    ```
2. Loop over the options (numbers in _A_), and build the paths (enumerations)
    ```python
    for i, num in enumerate(options):
        dfs(options[:i] + options[i+1:], path + [num])
    ```

## Code Dissection - permutations
1. Create a list to store the result, run `dfs()`, then return the result
    ```python
    result = []
    dfs(A, [])
    return result
    ```