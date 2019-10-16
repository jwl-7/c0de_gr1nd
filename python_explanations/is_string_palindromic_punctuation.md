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
* The solution uses a start and end pointer to check if the string is palindromic in-place
* The pythonic solution converts the string to a list of alphanumeric-only characters and uses list slicing to check if the list is palindromic
* `str.isalnum()` returns true if all characters in _str_ are alphanumeric
* `str.lower()` returns a copy of _str_ with lowercase characters

## Code Dissection
1. Create a start and end pointer that correlate to the start and end index of the string
    ```python
    start = 0
    end = len(s) - 1
    ```
2. Loop through the string until the two pointers meet in the middle, which is the case if the string is a palindrome
    ```python
    while start < end:
    ```
3. Check if the characters at the start and end pointers are alphanumeric
    ```python
    while start < end and not s[start].isalnum():
        start += 1
    while start < end and not s[end].isalnum():
        end -= 1
    ```
    * The start and end pointers are incremented/decremented to skip over the non-alphanumeric characters
4. Check if the characters at the start and end pointers are the same
    ```python
    if s[start].lower() != s[end].lower():
        return False
    ```
    * If the two characters are not the same, then we know the string is not a palindrome
    * `lower()` is used, because the uppercase and lowercase of a letter do not have equal values
5. If the characters at the two pointers are equal, continue checking the string
    ```python
    start += 1
    end -= 1
    ```
6. Return `True` if the two pointers meet and the function breaks out of the while loop, because that means the string is palindromic
    ```python
    return True
    ```

## Pythonic Code Dissection
1. Use slice notation to generate a copy of the string without non-alphanumeric characters
    ```python
    s = [x.lower() for x in s if x.isalnum()]
    ```
2. Return the comparison of the new _s_ to the reverse of _s_
    ```python
    return s == s[::-1]
    ```