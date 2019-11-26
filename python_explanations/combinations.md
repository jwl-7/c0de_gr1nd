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
* For an explanation on computing all possible subsets: [Generate the Power Set](#power_set.md)
* Use the same method as computing all possible subsets, except restrict the result to those subsets of size _k_

## Code Dissection
1. BLANK