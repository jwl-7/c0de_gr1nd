# Check if a Decimal Integer is a Palindrome  

"A palindromic string is one which reads the same forwards and backwards, e.g., 'redivider'." - EPI  
  
Problem:  
Write a program that takes an integer and determines if that integer's representation as a decimal string is a palindrome.  
  
Examples:  
```
0    -> True
11   -> True
215  -> False
-1   -> False
777  -> True
```  
  
Solution - from [is-number-palindromic-mysol.py](is-number-palindromic-mysol.py):  
```python
def is_palindrome_number(x):
    if x < 0:
        return False
    reverse = str(x)[::-1]
    if x == int(reverse):
        return True
    else:
        return False
```  
  
Explanation:  
  
Python Slicing can be used for strings, lists, tuples, arrays, and custom data structures.  
  
The slicing notation follows the syntax: ```a[start:stop:step]```  
  
```a[::-1]``` steps backwards through the entirety of a, and thus reverses a.  
  
1. Check if the number (x) is negative, because a negative number in its string representation cannot be palindromic, since it starts with a -   
2. Convert the number (x) to a string and grab the reversed representation  
    ```python
    reverse = str(x)[::-1]
    ```  
3. If the original number (x) is the same as the reversed number (reverse), then it is a palindrome, else it is not
    ```python
    if x == int(reverse):
        return True
    else:
        return False
    ```  