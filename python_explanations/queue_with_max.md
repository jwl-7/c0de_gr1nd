# Implement a Queue with Max API
Implement a queue with enqueue, dequeue, and max operations. The max operation returns the maximum element currently stored in the queue.

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


class QueueWithMax:

    def __init__(self):
        self.input = Stack()
        self.output = Stack()

    def enqueue(self, x):
        self.input.push(x)

    def dequeue(self):
        if self.output.empty():
            while not self.input.empty():
                self.output.push(self.input.pop())
        if not self.output.empty():
            return self.output.pop()

    def max(self):
        if not self.input.empty():
            if self.output.empty():
                return self.input.max()
            else:
                return max(self.input.max(), self.output.max())
        elif not self.output.empty():
            return self.output.max()
```

## Explanation
* For an explanation on the `Stack` and `Queue` classes:
    1. [Implement a Stack with Max API](stack_with_max.md)
    2. [Implement a Queue Using Stacks](queue_from_stacks.md)
* The solution combines the implementation of a stack with a `max()` function and a queue using two stacks

## Code Dissection - max
1. Check if the input stack is not empty
    ```python
    if not self.input.empty():
    ```
    1. If the output stack is empty, return the input stack's max
        ```python
        if self.output.empty():
            return self.input.max()
        ```
    2. If the output stack is not empty, return the max of input stack's max and output stack's max
        ```python
        else:
            return max(self.input.max(), self.output.max())
        ```
2. If the input stack is empty, but the output stack is not empty, return the output stack's max
    ```python
    elif not self.output.empty():
        return self.output.max()
    ```