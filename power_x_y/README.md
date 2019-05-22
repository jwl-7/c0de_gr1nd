# Compute x<sup>y</sup>  
  
Problem:  
Write a program that takes a double x and an integer y and returns x<sup>y</sup>. You can ignore overflow and underflow.     
  
Examples:  
```
 Input: x = 9.871778445549765, y = 3
Output: 962.0246486149941

 Input: x = 1.0005205926241314, y = 2
Output: 1.001041456264943

 Input: x = 3.398860582608009, y = 4
Output: 133.45455538332973
```  
  
Solution - from [power-x-y-mysol.py](power-x-y-mysol.py):  
```python
def power(x, y):
    result = 1
    if y < 0:
        y = -y
        x = 1 / x
    while y:
        if y & 1:
            result *= x
        x *= x
        y >>= 1
    return result
```  
  
Explanation:  
  
1. Initialize the result to 1  
2. If the power (y) is negative, get the absolute value of y, and replace x with 1 / x  
    ```python
    if y < 0:
        y = -y
        x = 1 / x
    ```  
3. Loop over the power (y)  
    a. If y is odd, set the result = result * the base (x)  
    ```python
    if y & 1:
        result *= x
    ```  
    b. Set the base (x) = x * x, and divide the power (y) in half  
    ```python
    x *= x
    y >>= 1
    ```  
4. Return the result (also sometimes referred to as the power)  
  
</br>  
  
[Python Bitwise Operators Reference](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)