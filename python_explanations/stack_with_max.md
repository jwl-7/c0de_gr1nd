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
* BLANK
  
## Code Dissection
1. BLANK