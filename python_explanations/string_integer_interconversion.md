# Interconvert Strings and Integers
Write a function to convert an integer to a string, and another function to convert a string to an integer.

## Examples
```
String to Integer Function:
    Input: "724"
   Output: 724

    Input: "-341"
   Output: -341

Integer to String Function:
    Input: 245
   Output: "245"

    Input: -132
   Output: "-132"
```

## Solution
```python
def int_to_string(x):
    is_negative = False
    if x < 0:
        x = -x
        is_negative = True

    s = []
    while True:
        s.append((chr(ord('0') + x % 10)))
        x //= 10
        if x == 0:
            break
    return ('-' if is_negative else '') + ''.join(s[::-1])


def string_to_int(s):
    is_negative = False
    if s[0] == '-':
        s = s[1:]
        is_negative = True

    result = 0
    for i in range(len(s)):
        result = result * 10 + (ord(s[i]) - ord('0'))
    return -result if is_negative else result
```

## Explanation
* Both functions rely on building each digit one at a time
* Converting integer to string:
    * For any positive integer _x_, the least significant digit in the decimal representation of _x_ is _x_ mod 10, and the remaining digits are _x_ &#8725; 10
    * This method computes the digits in reverse order
* Converting string to integer:
    * The solution is to begin from the leftmost digit and with each succeeding digit, multiply the partial result by 10 and add that digit

## Code Dissection - int_to_string
1. Check if the integer is negative, set a boolean accordingly, and set the integer to positive if needed
    ```python
    is_negative = False
    if x < 0:
        x = -x
        is_negative = True
    ```
2. Iterate through the number, and add each digit to the end of a list
    ```python
    while True:
        s.append((chr(ord('0') + x % 10)))
        x //= 10
        if x == 0:
            break
    ```
    * `chr(i)` returns a string of one character whose ASCII code is the integer _i_
    * `ord('a')` returns an integer representing the ASCII code of the character
    * `chr(i)` and `ord('a')` are the inverse of each other
3. Return the list with the computed digits in a reversed string with the correct sign
    ```python
    return ('-' if is_negative else '') + ''.join(s[::-1])
    ```
    * Python slicing notation follows the syntax: `a[start:stop:step]`
    * `a[::-1]` steps backwards through the entirety of a, thus reversing a

## Code Dissection - string_to_int
1. Check if the number is negative, set a boolean accordingly, and remove the sign character from the string if needed
    ```python
    is_negative = False
    if s[0] == '-':
        s = s[1:]
        is_negative = True
    ```
2. Iterate through all the characters of the string and update the result
    ```python
    result = 0
    for i in range(len(s)):
        result = result * 10 + (ord(s[i]) - ord('0'))
    ```
3. Return the integer with the correct sign
    ```python
    return -result if is_negative else result
    ```