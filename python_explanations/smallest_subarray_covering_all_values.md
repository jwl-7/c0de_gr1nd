# Find Smallest Subarray Sequentially Covering All Values
Given an array of strings and a set of strings, return the starting/ending indices of the shortest subarray that contains the set. The strings in the subarray must occur in sequential order.

## Examples
```
 Input: paragraph = ['a', 'b', 'd', 'f', 'g', 'c', 'a', 'd']
         keywords = ['a', 'b', 'c']
Output: Subarray(start=0, end=5)

 Input: paragraph = ['dog', 'cat', 'dog', 'banana', 'cat', 'dog']
         keywords = ['banana', 'cat', 'dog']
Output: Subarray(start=3, end=5)
```

## Solution
```python
def find_smallest_sequentially_covering_subset(paragraph, keywords):
    key_lookup = {}
    for i, s in enumerate(keywords):
        key_lookup[s] = i
    recent = [-1] * len(keywords)
    smallest = [float('inf')] * len(keywords)
    shortest = float('inf')
    start, end = 0, 0

    for i, s in enumerate(paragraph):
        if s in key_lookup:
            key_idx = key_lookup[s]
            if key_idx == 0:
                smallest[key_idx] = 1
            elif smallest[key_idx - 1] != float('inf'):
                prev = i - recent[key_idx - 1]
                smallest[key_idx] = prev + smallest[key_idx - 1]
            recent[key_idx] = i
            if key_idx == len(keywords) - 1 and smallest[-1] < shortest:
                shortest = smallest[-1]
                start, end = i - shortest + 1, i
    return Subarray(start, end)
```

## Explanation
While iterating through the paragraph, there are lots of things to keep track of/compute, which is where hash tables come in handy:
* Lookup table that maps each keyword to its index in _keywords_
* Hash table that maps each keyword to its most recent occurrence in _paragraph_
* Hash table that maps each keyword _k_ to the shortest subarray that contains all the keywords up to _k_
* The smallest subarray found so far
* The start/end indices of the smallest subarray found so far

The algorithm is as follows:
1. Iterate through the paragraph to find matching keywords
2. For each keyword, look up its index in the lookup table, then compute its previous distance to its previous occurrence
3. Update the smallest subarray that contains all the keywords up to _k_
4. Update the index of the keyword's most recent occurrence
5. If the keyword is the last element in the lookup table, compare its corresponding smallest subarray to the smallest subarray found so far
    * In other words, once we find the smallest subarray, compare it to the previous one we found if it exists
6. Keep track of the start/end indices of the smallest subarray

## Code Dissection
1. Create a lookup table that maps each keyword to its index in _keywords_
    ```python
    key_lookup = {}
    for i, s in enumerate(keywords):
        key_lookup[s] = i
    ```
2. Create an array to hold the most recent occurrence of a keyword as we traverse through _paragraph_
    ```python
    recent = [-1] * len(keywords)
    ```
3. For each keyword _k_, keep track of the smallest subarray that ends at the most recent occurrence&mdash;the subarray includes the previous keywords up to _k_ in _keywords_
    ```python
    smallest = [float('inf')] * len(keywords)
    ```
4. Keep track of the smallest subarray up to the most recent occurrence of the last element in _keywords_ and the start/end indices of the smallest subarray
    ```python
    shortest = float('inf')
    start, end = 0, 0
    ```
5. Iterate over _paragraph_ and look for strings matching those in _keywords_
    ```python
    if s in key_lookup:
        key_idx = key_lookup[s]
    ```
6. If the keyword is the first element in *key_lookup*, then set its smallest subarray to 1
    ```python
    if key_idx == 0:
        smallest[key_idx] = 1
    ```
7. If the keyword is any other element in *key_lookup*, find the previous distance to its most recent occurrence, then update its corresponding entry in _smallest_
    ```python
    elif smallest[key_idx - 1] != float('inf'):
        prev = i - recent[key_idx - 1]
        smallest[key_idx] = prev + smallest[key_idx - 1]
    ```
8. For each keyword, update the index of its most recent occurrence
    ```python
    recent[key_idx] = i
    ```
9. If the keyword found is the last element in _keywords_ and its corresponding smallest subarray is smaller than the current, then update the smallest subarray found
    ```python
    if key_idx == len(keywords) - 1 and smallest[-1] < shortest:
        shortest = smallest[-1]
        start, end = i - shortest + 1, i
    ```
10. Return the start and end indices of the smallest subarray with the keywords in sequential order
    ```python
    return Subarray(start, end)
    ```