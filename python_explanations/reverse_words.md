# Reverse All the Words in a Sentence
Given a string containing a set of words separated by whitespace, we would like to transform it to a string in which the words appear in reverse order. We do not need to keep the original string.  
  
Implement a function for reversing the words in a string _s_. Assume _s_ is a string encoded as a bytearray.  
  
## Examples
```
 Input: 'Silence is peaceful'
Output: 'peaceful is Silence'

 Input: 'Alice likes Bob'
Output: 'Bob likes Alice'
```
  
## Solution
```python
def reverse_words(s):
    s[:] = s[::-1]
    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            if start > 0:
                s[start:] = s[end:start-1:-1]
            else:
                s[start:] = s[::-1]
            break
        if start < end:
            if start == 0:
                s[start:end] = s[end-1::-1]
            else:
                s[start:end] = s[end-1:start-1:-1]
        start = end + 1
```
  
## Pythonic Solution
```python
def reverse_words_pythonic(s):
    s[:] = b' '.join(word[::-1] for word in s[::-1].split(b' '))
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK