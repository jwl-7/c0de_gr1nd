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

## Code Dissection
1. BLANK