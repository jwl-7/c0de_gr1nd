# Reverse Digits  
  
Problem:  
Write a program which takes an integer and returns the integer corresponding to the digits of the input written in reverse order.  
  
Examples:  
```
42   -> 24  
-314 -> -413  
2117 -> 7112  
-94  -> -49  
```  
  
Solution - from [reverse-digits-mysol.py](reverse-digits-mysol.py):  
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
  
Explanation:  
1. If the number (x) is negative, get the absolute value of x, convert to string, reverse the digits, convert back to a negative integer, and return the reversed number.  
    ```python
    if x < 0:
        x = str(abs(x))[::-1]
        x = -int(x)
        return x
    ```  
2. Else if the number (x) is positive, convert to string, reverse the digits, and return the reversed number in an integer.  
    ```python
    else:
        x = str(x)[::-1]
        return int(x)
    ```  
  
</br>  
  
[Python Bitwise Operators Reference](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)