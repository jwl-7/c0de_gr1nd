# Evaluate RPN Expressions
Given an expression written in Reverse Polish Notation (RPN), compute the value.

## Examples
```
 Input: '10,7,*'
Output: 70

 Input: '999,120,/,111,1007,/,+'
Output: 8
```

## Solution
```python
def evaluate(expression):
    stack = []
    operators = '+-*/'
    for token in expression.split(','):
        if token not in operators:
            stack.append(int(token))
        else:
            y = stack.pop()
            x = stack.pop()
            if token == '+':
                result = x + y
            elif token == '-':
                result = x - y
            elif token == '*':
                result = x * y
            elif token == '/':
                result = int(x / y)
            stack.append(result)
    return stack[0]
```

## Explanation
* The solution uses the [Postfix evaluation algorithm](https://en.wikipedia.org/wiki/Reverse_Polish_notation#Explanation)

The pseudocode for the algorithm is as follows:
```python
for each token in the postfix expression:
    if token is an operator:
        operand_2 <- pop from the stack
        operand_2 <- pop from the stack
        result <- evaluate token with operand_1 and operand_2
        push result back onto the stack
    else if token is an operand:
        push token onto the stack
result <- pop from the stack
```

## Code Dissection
1. Create an empty stack and a string that contains the arithmetic operators
    ```python
    stack = []
    operators = '+-*/'
    ```
2. Loop over each comma separated token in the expression
    ```python
    for token in expression.split(','):
    ```
3. If the token is a number, push it to the stack
    ```python
    if token not in operators:
        stack.append(int(token))
    ```
4. If the token is an operator, then pop two operands off the stack
    ```python
    y = stack.pop()
    x = stack.pop()
    ```
5. Depending on the operator, perform the appropriate computation, and push the result to the stack
    ```python
    if token == '+':
        result = x + y
    elif token == '-':
        result = x - y
    elif token == '*':
        result = x * y
    elif token == '/':
        result = int(x / y)
    stack.append(result)
    ```
    * `int(x / y)` is used, because the problem only wants integers as answers
6. Return the final result from the stack
    ```python
    return stack[0]
    ```
    * We could also pop this result from the stack, but there is no need to