# Test a String over "{,},(,),[,]" for Well-Formedness
A string over the characters "{,},(,),[,]" is said to be well-formed if the different types of brackets match in the correct order.
  
Write a program that tests if a string made up of the characters '(',')','[',']',"{' and "}' is well-formed.
  
## Examples
```
 Input: '[()[]]{}'
Output: True

 Input: '{[{}}]'
Output: False
```
  
## Solution
```python
def is_well_formed(s):
    stack = []
    brackets = {
        '[': ']',
        '(': ')',
        '{': '}'
    }
    for char in s:
        if char in brackets:
            stack.append(char)
        elif not stack or char != brackets[stack.pop()]:
            return False
    return not stack
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK