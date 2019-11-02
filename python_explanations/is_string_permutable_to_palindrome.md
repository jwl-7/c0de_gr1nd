# Test for Palindromic Permutations
Write a program to test whether the letters forming a string can be permuted to form a palindrome.

## Examples
```
 Input: 'ya a rrya'
Output: True

 Input: 'itnrsg'
Output: False
```

## Solution
```python
def can_form_palindrome(s):
    odd = 0
    for count in collections.Counter(s).values():
        if count % 2:
            odd += 1
    return odd <= 1
```

## Explanation
* BLANK

## Code Dissection
1. BLANK