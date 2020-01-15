# Transform One String to Another
Given two words _s_ and _t_ and a dictionary _D_, compute the length of the shortest transformation sequence from _s_ to _t_.

* Change only one letter at a time
* Each transformation must exist in the dictionary
* Return -1 if no transformation is possible
* Each word in the dictionary is the same length

## Examples
```
 Input: s = 'car', t = 'dog'
        D = ['cat', 'dog', 'cog', 'cot', 'log']
Output: 4

Transformation: 'car' -> 'cat' -> 'cot' -> 'cog' -> 'dog'


 Input: s = 'car', t = 'bat'
        D = ['log', 'dog', 'bar', 'cat', 'rat']
Output: -1

'bat' is not in the dictionary, thus no transformation is possible.
```

## Solution
```python
def transform_string(D, s, t):
    q = collections.deque([(s, 0)])
    visited = set()
    while q:
        word, dist = q.popleft()
        if word == t:
            return dist
        for i in range(len(word)):
            for j in string.ascii_lowercase:
                nxt_word = word[:i] + j + word[i+1:]
                if nxt_word not in visited and nxt_word in D:
                    q.append((nxt_word, dist + 1))
                    visited.add(nxt_word)
    return -1
```

## Explanation
* Perform a BFS, search for a transformation that is in the dictionary, then continue while keeping a cache of the visited words

## Code Dissection
1. Create a queue to iterate through the candidate words / keep track of distances and a cache for the visited words in the dictionary
    ```python
    q = collections.deque([(s, 0)])
    visited = set()
    ```
2. While the queue isn't empty, grab the word/distance from it, and check if its our target word _t_
    ```python
    while q:
        word, dist = q.popleft()
        if word == t:
            return dist
    ```
3. Search for a candidate transformation word using the alphabet
    ```python
    for i in range(len(word)):
        for j in string.ascii_lowercase:
            nxt_word = word[:i] + j + word[i+1:]
    ```
4. If we find a candidate that's in the dictionary _D_ and has not been used, then add it to the queue and cache
    ```python
    if nxt_word not in visited and nxt_word in D:
        q.append((nxt_word, dist + 1))
        visited.add(nxt_word)
    ```
5. If there is no transformation sequence from _s_ to _t_, then return -1
    ```python
    return -1
    ```