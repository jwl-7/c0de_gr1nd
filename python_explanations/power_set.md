# Generate the Power Set
Given a set of distinct integers, return all possible subsets.

## Example
```
 Input: [0, 1, 2]
Output: [[], [0], [1], [2], [0, 1], [1, 2], [0, 2], [0, 1, 2]]
```

## Solution
```python
def generate_power_set(S):
    def dfs(options, path):
        result.append(path)
        for i, num in enumerate(options):
            dfs(options[i+1:], path + [num])

    result = []
    dfs(S, [])
    return result
```

## Explanation
* For any set _S_ with _n_ elements, there are 2<sup>_n_</sup> subsets where each number is in the range [0, 2<sup>_n_-1</sup>]

## Code Dissection - dfs
1. Add the current path to the result list
    ```python
    result.append(path)
    ```
2. Loop over the options (numbers in _S_), and build the paths (enumerations)
    ```python
    for i, num in enumerate(options):
        dfs(options[i+1:], path + [num])
    ```

## Code Dissection - generate_power_set
1. Create a list to store the result, run `dfs()`, then return the result
    ```python
    result = []
    dfs(S, [])
    return result
    ```