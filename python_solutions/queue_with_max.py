from test_framework import generic_test
from test_framework.test_failure import TestFailure


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


def queue_tester(ops):

    try:
        q = QueueWithMax()

        for (op, arg) in ops:
            if op == 'QueueWithMax':
                q = QueueWithMax()
            elif op == 'enqueue':
                q.enqueue(arg)
            elif op == 'dequeue':
                result = q.dequeue()
                if result != arg:
                    raise TestFailure("Dequeue: expected " + str(arg) +
                                      ", got " + str(result))
            elif op == 'max':
                result = q.max()
                if result != arg:
                    raise TestFailure(
                        "Max: expected " + str(arg) + ", got " + str(result))
            else:
                raise RuntimeError("Unsupported queue operation: " + op)
    except IndexError:
        raise TestFailure('Unexpected IndexError exception')


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("queue_with_max.py",
                                       'queue_with_max.tsv', queue_tester))
