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
* BLANK

## Code Dissection
1. BLANK