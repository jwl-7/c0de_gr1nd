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
1. The string is processed one bracket at a time starting from the left
2. If the character is an open bracket, it is pushed to the stack
3. If the character is a close bracket:
    1. The stack is empty - the string is False
    2. The close bracket does not match the open bracket popped off the stack - the string is False
4. After processing the string, if the stack is empty, then the string is well-formed
  
## Code Dissection
1. Create an empty stack and a dictionary with the open/close brackets
    ```python
    stack = []
    brackets = {
        '[': ']',
        '(': ')',
        '{': '}'
    }
    ```
2. Loop over each character in the string
    ```python
    for char in s:
    ```
3. If the character is an open bracket, push it to the stack
    ```python
    if char in brackets:
        stack.append(char)
    ```
4. If the character is a close bracket, check if the stack is empty or if the close bracket matches the open bracket popped off the stack
    ```python
    elif not stack or char != brackets[stack.pop()]:
        return False
    ```
5. Return whether or not the stack is empty, with True being the case that the string is well-formed
    ```python
    return not stack
    ```