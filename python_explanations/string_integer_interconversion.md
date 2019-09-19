# Interconvert Strings and Integers
A string is a sequence of characters. A string may encode an integer, e.g., "123" encodes 123. In this problem, you are to implement methods that take a string representing an integer and return the corresponding integer, and vice versa. Your code should handle negative integers. You cannot use library functions like int in Python.  
  
Implement an integer to string conversion function, and a string to integer conversion function. For example, if the input to the first function is the integer 314, it should return the string "314" and if the input to the second function is the string "314" it should return the integer 314.  
  
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

    if is_negative:
        return '-' + ''.join(s[::-1])
    return ''.join(s[::-1])

def string_to_int(s):
    is_negative = False
    if s[0] == '-':
        s = s[1:]
        is_negative = True

    result = 0
    for i in range(len(s)):
        result = result * 10 + (ord(s[i]) - ord('0'))
        
    if is_negative:
        result = -result
    return result
```
  
## Explanation
* BLANK  
  
## Code Dissection
1. BLANK  