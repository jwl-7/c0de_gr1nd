# Generate All Subsets of Size _k_
Given two integers _n_ and _k_, return all size _k_ subsets of [1,..., _n_].

## Example
```
 Input: n = 4
        k = 2
Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
```

## Solution
```python
def combinations(n, k):
    def dfs(options, k, path):
        if k == 0:
            result.append(path)
            return
        for i, num in enumerate(options):
            dfs(options[i+1:], k - 1, path + [num])

    result = []
    dfs(range(1, n + 1), k, [])
    return result
```

## Explanation
* For an explanation on computing all possible subsets: [Generate the Power Set](power_set.md)
* Use the same method as computing all possible subsets, except restrict the result to those subsets of size _k_

## Code Dissection - dfs
1. If we've generated a subset of size _k_, then add it to the result
    ```python
    if k == 0:
        result.append(path)
        return
    ```
2. Loop over the options (numbers in [1,..., _n_]), and build the paths (subsets)
    ```python
    for i, num in enumerate(options):
        dfs(options[i+1:], k - 1, path + [num])
    ```

## Code Dissection - generate_power_set
1. Create a list to store the result, run `dfs()`, then return the result
    ```python
    result = []
    dfs(range(1, n + 1), k, [])
    return result
    ```