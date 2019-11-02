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

## Pythonic Solution
```python
def can_form_palindrome_pythonic(s):
    return sum(count % 2 for count in collections.Counter(s).values()) <= 1
```

## Explanation
For a string to be permutable into a palindrome:
1. If the string is of even length, each character should appear an even number of times
2. If the string is of odd length, all but one character should appear and even number of times

## Code Dissection
1. Initialize a counter to store the odd count
    ```python
    odd = 0
    ```
2. Loop over each character's count in the string
    ```python
    for count in collections.Counter(s).values():
    ```
3. If a character has an odd count, increment _odd_
    ```python
    if count % 2:
        odd += 1
    ```
4. Return whether or not the amount of odd character counts is less than or equal to 1
    ```python
    return odd <= 1
    ```

## Pythonic Code Dissection
1. Return whether or not the amount of odd character counts is less than or equal to 1
    ```python
    return sum(count % 2 for count in collections.Counter(s).values()) <= 1
    ```