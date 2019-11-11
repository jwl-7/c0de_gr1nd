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
* The solution uses a hash table for quick lookups of clients and a BST for quick lookups of credits

## Code Dissection - __init__
1. Initialize a credit offset, a hash table for clients, and a BST for credits
    ```python
    self.offset = 0
    self.clients = {}
    self.credits = SortedDict()
    ```
    * `offset` helps keep the correct credit amount after calls to `add_all()`
    * `clients` is a hash table with *client_id* as the key and credit as the value
    * `credits` is a BST with credit as the key and *client_id* as the value

## Code Dissection - insert
1. Call `remove()` just in case the client already exists
    ```python
    self.remove(client_id)
    ```
2. Add the *client_id* and credit to the hash table
    ```python
    self.clients[client_id] = c - self.offset
    ```
3. Add the credit and *client_id* to the BST
    ```python
    self.credits[c - self.offset] = client_id
    ```

## Code Dissection - remove
1. If the client isn't in the hash table, then return False
    ```python
    if client_id not in self.clients:
        return False
    ```
2. Grab the credit amount for the *client_id*
    ```python
    credit = self.clients[client_id]
    ```
3. If the credit amount doesn't have a *client_id* attached to it, then delete it from the BST
    ```python
    if not self.credits[credit]:
        del self.credits[credit]
    ```
4. Remove the client from the hash table and return True for a successful removal
    ```python
    del self.clients[client_id]
        return True
    ```

## Code Dissection - lookup
1. If the client isn't in the hash table, then return -1
    ```python
    if client_id not in self.clients:
        return -1
    ```
2. Grab the credit amount for the *client_id*
    ```python
    credit = self.clients[client_id]
    ```
3. Return the credit amount + the offset
    ```python
    return credit + self.offset
    ```

## Code Dissection - add_all
1. Add _C_ to the credit offset
    ```python
    self.offset += C
    ```

## Code Dissection - max
1. If the BST is empty, then return an empty string
    ```python
    if not self.credits:
        return ''
    ```
2. Return the *client_id* that holds the max credit value
    ```python
    return self.credits.peekitem(-1)[1]
    ```