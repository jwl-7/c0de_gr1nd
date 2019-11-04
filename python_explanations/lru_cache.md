# Implement an ISBN Cache
Design a cache for looking up the prices of books by their ISBN. Implement lookup, insert, and erase functions with an LRU cache policy.

## Solution
```python
class LruCache:

    def __init__(self, capacity):
        self.prices = collections.OrderedDict()
        self.capacity = capacity

    def lookup(self, isbn):
        if isbn not in self.prices:
            return -1
        self.prices.move_to_end(isbn, last=False)
        return self.prices[isbn]

    def insert(self, isbn, price):
        if isbn not in self.prices:
            if len(self.prices) == self.capacity:
                self.prices.popitem()
            self.prices[isbn] = price
        self.prices.move_to_end(isbn, last=False)

    def erase(self, isbn):
        return self.prices.pop(isbn, False) is not False
```

## Explanation
* BLANK

## Code Dissection
1. BLANK