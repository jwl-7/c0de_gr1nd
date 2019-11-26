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
* For an explanation on validating matching parentheses: [Test a String over "{,},(,),[,]" for Well-Formedness](is_valid_parenthesization.md)
* If we think back to the problem above we can make two observations of the solution:
    1. If we have two stacks: one for '(' and the other for ')', then a string is formed when both stacks are empty
    2. We only add from the right stack of ')', when the left stack of '(' is smaller

## Code Dissection - dfs
1. If the left and right stack are empty, then add the string to the result
    ```python
    if not left and not right:
        result.append(path)
        return
    ```
2. If _left_ > 0, then add _left_ number of '(' to the path
    ```python
    if left:
        dfs(left - 1, right, path + '(')
    ```
3. If _left_ < _right_, then add _right_ number of ')' to the path
    ```python
    if left < right:
        dfs(left, right - 1, path + ')')
    ```

## Code Dissection - generate_balanced_parentheses
1. Create a list to store the result, run `dfs()`, then return the result
    ```python
    result = []
    dfs(num_pairs, num_pairs, '')
    return result
    ```