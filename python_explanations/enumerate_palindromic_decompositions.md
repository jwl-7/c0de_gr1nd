# Generate Palindromic Decompositions
Given a string _s_, return all possible combinations of partitioning _s_ such that each substring is a palindrome.

## Example
```
 Input: 'aabbc'
Output: [['a', 'a', 'b', 'b', 'c'], ['a', 'a', 'bb', 'c'], ['aa', 'b', 'b', 'c'], ['aa', 'bb', 'c']]
```

## Solution
```python
def palindrome_decompositions(s):
    def dfs(s, path):
        if not s:
            result.append(path)
            return
        for i in range(1, len(s) + 1):
            if s[:i] == s[:i][::-1]:
                dfs(s[i:], path + [s[:i]])

    result = []
    dfs(s, [])
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK