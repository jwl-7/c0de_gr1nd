from test_framework import generic_test
from test_framework.test_failure import TestFailure


class Queue:

    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.num = 0

    def enqueue(self, x):
        if self.num == len(self.queue):
            self.queue = (self.queue[self.head:] + self.queue[:self.head])
            self.queue += [None] * len(self.queue)
            self.head = 0
            self.tail = self.num
        self.queue[self.tail] = x
        self.tail = (self.tail + 1) % len(self.queue)
        self.num += 1

    def dequeue(self):
        if self.num > 0:
            data = self.queue[self.head]
            self.head = (self.head + 1) % len(self.queue)
            self.num -= 1
            return data

    def size(self):
        return self.num


def queue_tester(ops):
    q = Queue(1)

    for (op, arg) in ops:
        if op == 'Queue':
            q = Queue(arg)
        elif op == 'enqueue':
            q.enqueue(arg)
        elif op == 'dequeue':
            result = q.dequeue()
            if result != arg:
                raise TestFailure(
                    "Dequeue: expected " + str(arg) + ", got " + str(result))
        elif op == 'size':
            result = q.size()
            if result != arg:
                raise TestFailure(
                    "Size: expected " + str(arg) + ", got " + str(result))
        else:
            raise RuntimeError("Unsupported queue operation: " + op)


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("circular_queue.py",
                                       'circular_queue.tsv', queue_tester))
