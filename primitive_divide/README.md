# Compute x / y
  
Problem:  
Given two positive integers, compute their quotient, using only the addition, subtraction, and shifting operators.   
  
Examples:  
```
12 / 4 = 3
7 / 7  = 1
10 / 5 = 2
42 / 7 = 6
```  
  
Solution - from [primitive-divide-mysol.py](primitive-divide-mysol.py):  
```python
def divide(x, y):
    quotient = 0
    while x >= y:
        y2 = y
        multiple = 1
        while x >= y2 << 1:
            multiple <<= 1
            y2 <<= 1
        quotient += multiple
        x -= y2
    return quotient
```  
  
Explanation:  
  
The approach is based off the brute-force solution where subtracting the divisor from the divident until the dividend < divisor results in the dividend = remainder, and the number of subtractions = quotient.  
  
1. Initialize quotient = 0  
2. Loop until the dividend (x) < divisor (y)  
    a. Create a temporary y and multiple variable - these will help with optimizing the solution  
    ```python
    y2 = y
    multiple = 1
    ```  
3. (Nested Loop) Loop until dividend (x) < temporary divisor (y2) * 2  
    ```python
    while x >= y2 << 1:
    ```  
    a. Set multiple = multiple * 2 and y2 = y2 * 2
    ```python
    multiple <<= 1
    y2 <<= 1
    ```  
4. Add the multiple to the quotient  
    ```python
    quotient += multiple
    ```
5. Subtract the temporary divisor (y2) from the dividend (x)  
    ```python
    x -= y2
    ```  
6. Return the quotient  
  
</br>  
  
[Python Bitwise Operators Reference](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)