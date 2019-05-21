# Compute x * y without Arithmetical Operators

"Sometimes the processors used in ultra low-power devices such as hearing aids do not have dedicated hardware for performing multiplication. A program that needs to perform  multiplication must do so explicitly using lower-level primitives." - EPI  
  
Problem:  
Write a program that multiplies two nonnegative integers. The only operators you are allowed to use are:  
* assignment  
* the bitwise operators >>, <<, |, &, ~, ^  
* equality checks and Boolean combinations thereof  
  
Examples:  
```
3 * 4  = 12
7 * 7  = 49
5 * 2  = 10
10 * 8 = 80
```  
  
Solution - from [primitive-multiply-mysol.py](primitive-multiply-mysol.py):  
```python
def add(x, y):
    while y != 0:
        carry = x & y
        x ^= y
        y = carry << 1
    return x
  
def multiply(x, y):
    product = 0
    while y != 0:
        if y & 1:
            product = add(product, x)
        x <<= 1
        y >>= 1
    return product
```  
  
Explanation:  
1. Write add function to be used in the multiply function  
    a. Loop until there is no carry  
    b. Set carry = common set bits of x and y  
    ```python
    carry = x & y
    ```  
    c. Get the sum of bits x and y  
    ```python
    x ^= y
    ```  
    d. Shift the carry into y, so that adding it to x gives the sum with the carry  
    ```python
    y = carry << 1
    ```  
    e. Return the sum  
2. Write multiply function using the shift and add algorithm  
    a. Initialize product = 0    
    b. Loop until y = 0  
    c. If y is 1, add the bit to the product  
    ```python
    if y & 1:
        product = add(product, x)
    ```  
    d. Left shift multiplicand (x = x * 2)  
    ```python
    x <<= 1
    ```  
    e. Right shift multiplier (y = y / 2)  
    ```python  
    y >>= 1
    ```  
    f. Return the product  
  
</br>  
  
[Python Bitwise Operators Reference](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)