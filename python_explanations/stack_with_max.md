# Implement a Stack with Max API
Design a stack with a max() function.

## Solution
```python
class Stack:

    def __init__(self):
        self.stack = []

    def empty(self):
        return self.stack == []

    def max(self):
        if self.stack:
            return self.stack[-1][1]

    def pop(self):
        if self.stack:
            return self.stack.pop()[0]

    def push(self, x):
        curr_max = max(x, self.stack[-1][1] if self.stack else x)
        self.stack.append((x, curr_max))
```

## Explanation
* The solution uses a stack where each element in the stack is a tuple in which the first element is the value pushed and the second element is the current max value

## Code Dissection - __init__
1. Initialize an empty stack
    ```python
    self.stack = []
    ```

## Code Dissection - empty
1. Return whether or not the stack is empty
    ```python
    return self.stack == []
    ```

## Code Dissection - max
1. Return the last element (tuple) on the stack, second element in the tuple
    ```python
    if self.stack:
        return self.stack[-1][1]
    ```

## Code Dissection - pop
1. Remove the last element (tuple) on the stack, and return the first element in the tuple
    ```python
    if self.stack:
        return self.stack.pop()[0]
    ```

## Code Dissection - push
1. Set the current max by getting the max of _x_ and the last element (tuple) on the stack, second element in the tuple
    ```python
    curr_max = max(x, self.stack[-1][1] if self.stack else x)
    ```
    * If the stack is empty, then the second argument in `max()` is _x_
2. Push _x_ and the current max as a tuple to the stack
    ```python
    self.stack.append((x, curr_max))
    ```