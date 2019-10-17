# Implement a Queue Using Stacks
Queue insertion and deletion follows first-in, first-out semantics; stack insertion and deletion is last-in, first-out.

How would you implement a queue given a library implementing stacks?

## Solution
```python
class Queue:

    def __init__(self):
        self.input = []
        self.output = []

    def enqueue(self, x):
        self.input.append(x)

    def dequeue(self):
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output.pop()
```

## Explanation
The solution uses two stacks:
1. The first stack is used to enqueue the elements, with the elements in LIFO order
2. The second stack is used to dequeue the elements, with the elements in FIFO order, by popping all the elements out of the first stack

## Code Dissection - __init__
1. Initialize an input stack to enqueue elements and an output stack to dequeue elements
    ```python
    self.input = []
    self.output = []
    ```

## Code Dissection - enqueue
1. Push _x_ to the _input_ stack
    ```python
    self.input.append(x)
    ```

## Code Dissection - dequeue
1. If the _output_ stack is empty, pop all the elements from the _input_ stack and push them to the _output_ stack
    ```python
    if not self.output:
        while self.input:
            self.output.append(self.input.pop())
    ```
2. Return the last element from the _output_ stack
    ```python
    return self.output.pop()
    ```