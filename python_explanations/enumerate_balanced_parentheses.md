# Generate Strings of Matched Parens
Given _n_ pairs of parentheses, return all combinations of strings with matching parentheses.

## Example
```
 Input: 3
Output: ['((()))', '(()())', '(())()', '()(())', '()()()']
```

## Solution
```python
def generate_balanced_parentheses(num_pairs):
    def dfs(left, right, path):
        if not left and not right:
            result.append(path)
            return
        if left:
            dfs(left - 1, right, path + '(')
        if left < right:
            dfs(left, right - 1, path + ')')

    result = []
    dfs(num_pairs, num_pairs, '')
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK