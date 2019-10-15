# Implement a Stack with Max API
Design a stack that includes a max operation, in addition to push and pop. The max method should return the maximum value stored in the stack.
  
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
  
## Code Dissection
1.  ```python
    def __init__(self):
        self.stack = []
    ```
    * This initializes the _Stack_ object with as an empty list
2.  ```python
    def empty(self):
        return self.stack == []
    ```
    * This returns whether or not the stack is empty
3.  ```python
    def max(self):
        if self.stack:
            return self.stack[-1][1]
    ```
    * This returns the last element (tuple) on the stack, second element in the tuple
4.  ```python
    def pop(self):
        if self.stack:
            return self.stack.pop()[0]
    ```
    * This removes the last element (tuple) on the stack and returns the first element in the popped tuple
5.  ```python
    def push(self, x):
        curr_max = max(x, self.stack[-1][1] if self.stack else x)
        self.stack.append((x, curr_max))
    ```
    * *curr_max* is set to the max of _x_ and the last element (tuple) on the stack, second element in the tuple
    * Each element on the stack is a tuple in the form of (value, current max value)