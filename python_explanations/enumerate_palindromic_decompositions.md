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
    def dfs(options, path):
        if not options:
            result.append(path)
            return
        for i in range(1, len(options) + 1):
            if options[:i] == options[:i][::-1]:
                dfs(options[i:], path + [options[:i]])

    result = []
    dfs(s, [])
    return result
```

## Explanation
* We loop over every possible substring and check if its a palindrome

## Code Dissection - dfs
1. If we run out of characters, then add the string to the result
    ```python
    if not options:
        result.append(path)
        return
    ```
2. Partition the string and test for palindromes
    ```python
    for i in range(1, len(options) + 1):
        if options[:i] == options[:i][::-1]:
            dfs(options[i:], path + [options[:i]])
    ```

## Code Dissection - palindrome_decompositions
1. Create a list to store the result, run `dfs()`, then return the result
    ```python
    result = []
    dfs(s, [])
    return result
    ```