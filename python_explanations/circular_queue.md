# Implement a Circular Queue
A queue can be implemented using an array and two additional fields, the beginning and the end indices. This structure is sometimes referred to as a circular queue. Both enqueue and dequeue have _O(1)_ time complexity. If the array is fixed, there is a maximum number of entries that can be stored. If the array is dynamically resized, the total time for _m_ combined enqueue and dequeue operations is _O(m)_.

Implement a queue API using an array for storing elements. Your API should include a constructor function, which takes as argument the initial capacity of the queue, enqueue and dequeue functions, and a function which returns the number of elements stored. Implement dynamic resizing to support storing an arbitrarily large number of elements.

## Solution
```python
class Queue:

    def __init__(self, capacity):
        self.queue = [None] * capacity
        self.head = 0
        self.tail = 0
        self.num = 0

    def enqueue(self, x):
        if self.num == len(self.queue):
            self.queue = (self.queue[self.head:] + self.queue[:self.head])
            self.queue += [None] * (len(self.queue) * 2 - len(self.queue))
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
```

## Explanation
* BLANK

## Code Dissection
1. BLANK