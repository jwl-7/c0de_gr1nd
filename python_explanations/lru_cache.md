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
* The ordered dictionary acts like a FIFO queue
* Looking up an ISBN number that exists moves the entry to the front of the queue

## Code Dissection - init
1. Create a hash table for the prices of the books and a variable to store the maximum size
    ```python
    self.prices = collections.OrderedDict()
    self.capacity = capacity
    ```

## Code Dissection - lookup
1. If the ISBN number can't be found, then return -1
    ```python
    if isbn not in self.prices:
        return -1
    ```
2. If the ISBN number exists, then move it to the front of the queue and return the price
    ```python
    self.prices.move_to_end(isbn, last=False)
    return self.prices[isbn]
    ```

## Code Dissection - insert
1. If the ISBN number is not in the table, check if the table is at max capacity first, then add the ISBN/price to the table
    ```python
    if isbn not in self.prices:
        if len(self.prices) == self.capacity:
            self.prices.popitem()
        self.prices[isbn] = price
    ```
    * Items get removed from the rear of the queue when inserting into a full table
2. If the ISBN number exists, don't change the price and move it to the front of the queue
    ```python
    self.prices.move_to_end(isbn, last=False)
    ```

## Code Dissection - erase
1. If the ISBN number exists, then remove it from the queue
    ```python
    return self.prices.pop(isbn, False) is not False
    ```
    * If the item does not exist, nothing changes, and the function returns False
    * If an item does get removed, the function returns True