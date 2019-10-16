# Evaluate RPN Expressions
A string is said to be an arithmetical expression in Reverse Polish notation (RPN) if:
1. It is a single digit or a sequence of digits, prefixed with an option &ndash;, e.g., "6", "123", "-42".
2. It is of the form "_A_, _B_, &#9900;", where _A_ and _B_ are RPN expressions and &#9900; is one of &plus;, &minus;, &times;, &#8725;.

For example, the following strings satisfy these rules: "1729", "3, 4, &plus;, 2, &times;, 1, &plus;", "1, 1, &plus;, -2, &times;", "-641, 6, &#8725;, 28, &#8725;".

An RPN expression can be evaluated uniquely to an integer, which is determined recursively. The base case corresponds to Rule 1, which is an integer expressed in base-10 positional system. Rule 2 corresponds to the recursive case, and the RPNs are evaluated in the natural way, e.g., if _A_ evaluates to 2 and _B_ evaluates to 3, then "_A_, _B_, &times;" evaluates to 6.

Write a program that takes an arithmetical expression in RPN and returns the number that the expression evaluates to.

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
1. Create an empty _stack_ and a string that contains the _operators_
    ```python
    stack = []
    operators = '+-*/'
    ```
2. Loop over each _token_ in the _expression_, which are separated by commas
    ```python
    for token in expression.split(','):
    ```
3. If the _token_ is a number, push it to the stack
    ```python
    if token not in operators:
        stack.append(int(token))
    ```
4. If the _token_ is an operator, then pop two operands off the stack
    ```python
    y = stack.pop()
    x = stack.pop()
    ```
5. Depending on the operator, use the appropriate computation for the result, and push the result to the stack
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
    * ```int(x / y)``` is used, because the problem only wants integers as answers
6. Return the final result in the stack
    ```python
    return stack[0]
    ```
    * We could also pop this result from the stack, but there is no need to