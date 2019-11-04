# Find the Nearest Repeated Entries in an Array
Given an array of strings, find the distance between the closest repeated words.

## Examples
```
 Input: ['foo', 'bar', 'asdf', 'foo', 'qwerty', 'qwerty', 'bar']
Output: 1

 Input: ['abc', 'def', 'qrz', 'abc', 'qwerty', 'asdf', 'foo']
Output: 3
```

## Solution
```python
def find_nearest_repetition(paragraph):
    table = {}
    closest = float('inf')
    for i, s in enumerate(paragraph):
        if s in table:
            distance = i - table[s]
            closest = min(closest, distance)
        table[s] = i
    return closest if closest != float('inf') else -1
```

## Explanation
* Each string (array element) and index are stored in a hash table
* If the string already exists in the table, compare the current index to the index in the table
* The minimum is computed between the distance between two matching words and the closest distance so far
* After comparing a duplicate, we no longer need to worry about the previous duplicate, so the entry is updated in the hash table

## Code Dissection
1. Create a hash table and a variable to store the closest distance so far
    ```python
    table = {}
    closest = float('inf')
    ```
    * _closest_ is initialized to infinity for the initial minimum calculation
2. Loop over each string (array element) and keep track of the indexes
    ```python
    for i, s in enumerate(paragraph):
    ```
3. If the string is in the hash table, compute the different between the current index and the one in the table, then compare the difference to the closest distance so far
    ```python
    if s in table:
        distance = i - table[s]
        closest = min(closest, distance)
    ```
4. If the string doesn't exist in the hash table, then add it with the index as the value
    ```python
    table[s] = i
    ```
    * If the string was already in the table, then the index is updated in the table after the comparisons
5. Return the closest distance between two duplicates
    ```python
    return closest if closest != float('inf') else -1
    ```
    * If there are no duplicates, then _closest_ needs to be changed from infinity to -1