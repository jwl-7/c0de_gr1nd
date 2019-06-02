# Reverse Digits
Write a program which takes an integer and returns the integer corresponding to the digits of the input written in reverse order.  
  
## Examples
```
42 -> 24
-94 -> -49
-314 -> -413
2117 -> 7112
```
  
## Solution
```python
def reverse(x):
    if x < 0:
        x = str(abs(x))[::-1]
        x = -int(x)
        return x
    else:
        x = str(x)[::-1]
        return int(x)
```
  
## Explanation
* The solution uses the brute-force algorithm, which is to convert the input to a string, reverse the string, and convert it back to an integer  
* Python slicing notation follows the syntax: ```a[start:stop:step]```  
* ```a[::-1]``` steps backwards through the entirety of a, thus reversing a  
  
## Code Dissection
1. If _x_ is negative, compute the absolute value of _x_, convert _x_ to a string, reverse the string, convert _x_ back into a negative integer, and return the input written in reverse order  
    ```python
    if x < 0:
        x = str(abs(x))[::-1]
        x = -int(x)
        return x
    ```
2. If _x_ is positive, convert _x_ to a string, reverse the string, convert _x_ back into an integer, and return the input written in reverse order  
    ```python
    else:
        x = str(x)[::-1]
        return int(x)
    ```