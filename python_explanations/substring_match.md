# Find the First Occurrence of a Substring
Given two strings _s_ (the "search string") and _t_ (the "text"), find the first occurrence of _s_ in _t_.
  
## Examples
```
Substring: 'zz'
     Text: '1234zz789'
   Output: 4

Substring: 'rs'
     Text: 'doghorsecat'
   Output: 5

Substring: 'asdfwqwe'
     Text: 'qwerty'
   Output: -1
```
  
## Solution
```python
def rabin_karp(t, s):
    m = len(s)
    n = len(t)
    d = 26
    q = 31
    s_hash = 0
    t_hash = 0
    h = 1

    if n < m:
        return -1

    h = (d ** (m - 1)) % q
    for i in range(m):
        s_hash = (d * s_hash + ord(s[i])) % q
        t_hash = (d * t_hash + ord(t[i])) % q

    for i in range(n - m + 1):
        if s_hash == t_hash and t[i:i+m] == s:
            return i
        if i < n - m:
            t_hash = (d * (t_hash - ord(t[i]) * h) + ord(t[i+m])) % q
    return -1
```
  
## Simple Solution
```python
def rabin_karp_simple(t, s):
    m = len(s)
    n = len(t)
    s_hash = hash(s)
    for i in range(n - m + 1):
        t_hash = hash(t[i:i+m])
        if t_hash == s_hash and t[i:i+m] == s:
            return i
    return -1
```
  
## Pythonic Solution
```python
def boyer_moore_horspool(t, s):
    return t.find(s)
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK
  
## Simple Code Dissection
1. BLANK
  
## Pythonic Code Dissection
1. BLANK