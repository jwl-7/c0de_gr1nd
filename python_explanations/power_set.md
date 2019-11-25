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
* BLANK

## Code Dissection
1. BLANK