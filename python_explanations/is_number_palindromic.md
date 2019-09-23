# Check if a Decimal Integer is a Palindrome
A palindromic string is one which reads the same forwards and backwards, such as the string 'racecar'.  
Write a program which determines if the decimal representation of an integer is a palindromic string.  
  
## Examples
```
0    -> True
11   -> True
215  -> False
-1   -> False
777  -> True
```
  
## Solution
```python
def is_palindrome_number(x):
    if x < 0:
        return False
    return x == int(str(x)[::-1])
```
  
## Explanation
* The solution uses a simple approach of comparing the integer _x_ to a copy of it in reverse order; if the two numbers are the same, then _x_ is a palindrome   
* Python slicing notation follows the syntax: ```a[start:stop:step]```  
* ```a[::-1]``` steps backwards through the entirety of a, thus reversing a  
  
## Code Dissection
1. If _x_ is negative, its decimal representation cannot be palindromic  
    ```python
    if x < 0:
        return False
    ```
2. Create a copy of the string representation of _x_ in reverse order  
    ```python
    reverse = str(x)[::-1]
    ```
3. If _x_ is equal to the decimal representation of reverse, then _x_ is palindromic, else it is not  
    ```python
    if x == int(reverse):
        return True
    else:
        return False
    ```