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
* The solution uses the [Rabin-Karp algorithm](https://en.wikipedia.org/wiki/Rabin%E2%80%93Karp_algorithm) that uses hashing to find patterns in strings
* The simple solution uses an interpretation of the Rabin-Karp algorithm with the help of the built-in ```hash()``` function
* The Pythonic solution simply uses the built-in ```find()``` function, which is documented to use the [Boyer-Moore-Horspool algorithm](https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore%E2%80%93Horspool_algorithm)

Simple overview of the Rabin-Karp string-searching algorithm:
1. A hash value is calculated for the substring to search for
2. A hash value is calculated for a 'window' of the text to search in
    * The window is the size of the substring
3. The substring hash and the current 'window' hash of the text are compared
4. If there is a match, the substring is in the text
    * To ensure a match is not a hash collision, the match should be compared to the substring
5. If there is no match, we slide the 'window' over by one character and recalculate the 'window' hash using the previous hash value
    * This is referred to as the rolling hash technique
    * Using a rolling hash allows us to avoid having to rehash the entire string

## Code Dissection
1. Create all the necessary variables to implement the Rabin-Karp algorithm:
    ```python
    m = len(s)
    n = len(t)
    d = 26
    q = 31
    s_hash = 0
    t_hash = 0
    h = 1
    ```
    * _s_ = substring to search for
    * _t_ = text to search in
    * _m_ = length of substring
    * _n_ = length of text
    * _d_ = number of chararacters in alphabet
    * _q_ = a prime number
    * *s_hash* = hash value of the substring
    * *t_hash* = hash value of the text
    * _h_ = value used when rehashing to help remove the leading digit
2. Check that the substring is not longer than the text, which is the case that the substring cannot exist
    ```python
    if n < m:
        return -1
    ```
3. Implement the formula _h_ = _d_ <sup>(_m_ - 1)</sup> mod _q_
    ```python
    h = (d ** (m - 1)) % q
    ```
4. Calculate the hash value for the substring and the first window of text
    ```python
    for i in range(m):
        s_hash = (d * s_hash + ord(s[i])) % q
        t_hash = (d * t_hash + ord(t[i])) % q
    ```
    * The first 'window' of text is the same size as the substring
5. Slide the substring over the text one-by-one
    ```python
    for i in range(n - m + 1):
    ```
6. If the two hash values match, return the index of the match
    ```python
    if s_hash == t_hash and t[i:i+m] == s:
        return i
    ```
    * ```t[i:i+m] == s``` is a brute-force comparison of the match to the substring -- this is to make sure that the match is not a hash collision
7. If the two hash values do not match, calculate the hash values for the next window
    ```python
    if i < n - m:
        t_hash = (d * (t_hash - ord(t[i]) * h) + ord(t[i+m])) % q
    ```
    * ```d *``` shifts left by 1 digit
    * ```t_hash - ord(t[i]) * h``` removes the leading (high-order) digit
    * ```+ ord(t[i+m])``` adds the trailing (low-order) digit
    * ```% q``` completes the formula, also helps prevent negative hash values
8. Implement the base case of the substring not being found
    ```python
    return -1
    ```

## Simple Code Dissection
1. Create all the necessary variables to implement the Rabin-Karp algorithm:
    ```python
    m = len(s)
    n = len(t)
    s_hash = hash(s)
    ```
    * _m_ = length of substring
    * _n_ = length of text
    * *s_hash* = hash value of the substring
2. Slide the substring over the text one-by-one
    ```python
    for i in range(n - m + 1):
    ```
3. Create (or rehash) the hash value of the text
    ```python
    t_hash = hash(t[i:i+m])
    ```
4. If the two hash values match, return the index of the match
    ```python
    if s_hash == t_hash and t[i:i+m] == s:
        return i
    ```
    * ```t[i:i+m] == s``` is a brute-force comparison of the match to the substring -- this is to make sure that the match is not a hash collision
5. Implement the base case of the substring not being found
    ```python
    return -1
    ```

## Pythonic Code Dissection
1. Completely disregard trying to figure out complicated mathematical algorithms for finding substrings and just use the built-in function ```find()``` like a normal person
    ```python
    return t.find(s)
    ```

## Useful References
* [Rip Tutorial - Introduction to Rabin-Karp Algorithm](https://riptutorial.com/algorithm/example/24653/introduction-to-rabin-karp-algorithm)
* [Brilliant - Rabin-Karp Algorithm](https://brilliant.org/wiki/rabin-karp-algorithm/)