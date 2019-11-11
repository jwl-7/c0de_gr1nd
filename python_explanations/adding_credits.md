# Add Credits
Design a credit system. Implement insert, remove, lookup, add-to-all, and max functions.

## Solution
```python
class ClientsCreditsInfo:

    def __init__(self):
        self.offset = 0
        self.clients = {}
        self.credits = SortedDict()

    def insert(self, client_id, c):
        self.remove(client_id)
        self.clients[client_id] = c - self.offset
        self.credits[c - self.offset] = client_id

    def remove(self, client_id):
        if client_id not in self.clients:
            return False
        credit = self.clients[client_id]
        if not self.credits[credit]:
            del self.credits[credit]
        del self.clients[client_id]
        return True

    def lookup(self, client_id):
        if client_id not in self.clients:
            return -1
        credit = self.clients[client_id]
        return credit + self.offset

    def add_all(self, C):
        self.offset += C

    def max(self):
        if not self.credits:
            return ''
        return self.credits.peekitem(-1)[1]
```

## Explanation
* BLANK

## Code Dissection - __init__
1. BLANK

## Code Dissection - insert
1. BLANK

## Code Dissection - remove
1. BLANK

## Code Dissection - lookup
1. BLANK

## Code Dissection - add_all
1. BLANK

## Code Dissection - max
1. BLANK