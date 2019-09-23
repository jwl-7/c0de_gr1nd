# Test Palindromicity
For the purpose of this problem, define a palindromic string to be a string which when all the nonalphanumeric are removed it reads the same front to back ignoring case.  
  
Implement a function which takes as input a string _s_ and returns true if _s_ is a palindromic string.  
  
## Examples
```
 Input: 'A man, a plan, a canal, Panama.'
Output: true

 Input: ';({Z'
Output: true

 Input: '~Z!@QE8Y'
Output: false
```
  
## Solution
```python
def is_palindrome(s):
    start = 0
    end = len(s) - 1
    while start < end:
        while start < end and not s[start].isalnum():
            start += 1
        while start < end and not s[end].isalnum():
            end -= 1
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1
    return True
```
  
## Pythonic Solution
```python
def is_palindrome_pythonic(s):
    s = [x.lower() for x in s if x.isalnum()]
    return s == s[::-1]
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK