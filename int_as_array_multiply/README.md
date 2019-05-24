# Multiply Two Arbitrary-Precision Numbers    
  
Problem:  
Write a program that takes two arrays representing integers, and returns an integer representing their product.     
    
Examples:  
```  
[1, 2, 3] * [3, 2, 1] = [3, 9, 4, 8, 3]

[7, 0, 4, 9] * [1, 9, 8, 4] = [1, 3, 9, 8, 5, 2, 1, 6]

[1, 2, 3, 4, 5, 6, 7] * [7, 6, 5, 4, 3, 2, 1] = [9, 4, 4, 9, 7, 7, 2, 1, 1, 4, 0, 0, 7]
```  
    
Solution - from [int-as-array-multiply-mysol.py](int-as-array-multiply-mysol.py):  
```python
def remove_leading_zeroes(num):
    i = 0
    length = len(num) - 1
    while i < length and num[0] == 0:
        num.remove(0)
        i += 1
    return num

def multiply(num1, num2):
    negative = False
    if num1[0] < 0 or num2[0] < 0:
        negative = True
        if num1[0] < 0 and num2[0] < 0:
            negative = False
        num1[0] = abs(num1[0])
        num2[0] = abs(num2[0])

    product = [0] * len(num1 + num2)
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
            product[i + j + 1] += num1[i] * num2[j]
            product[i + j] += product[i + j + 1] // 10
            product[i + j + 1] %= 10

    product = remove_leading_zeroes(product)
    if negative:
        product[0] = -product[0]
    return product
```  
  
Explanation:  
  
The approach is based off the grade school algorithm for multiplication.  
  
For instance, to compute 123 * 321:  
```
123 * 1 = 123
123 * 2 * 10 = 2460
123 * 3 * 100 = 36900
123 + 2460 + 36900 = 39483
```  
  
1. Check if the numbers at num1[0] and num2[0] are negative, set a boolean accordingly, and set both numbers to their absolute value      
    ```python
    negative = False
    if num1[0] < 0 or num2[0] < 0:
        negative = True
        if num1[0] < 0 and num2[0] < 0:
            negative = False
        num1[0] = abs(num1[0])
        num2[0] = abs(num2[0])
    ```  
2. Create an array for the product, which will be at most n + m digits  
    ```python
    product = [0] * len(num1 + num2)
    ```  
3. You need to loop over both arrays and keep in mind that the product is computed in reverse  
    ```python
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
    ```  
    a. Multiply num1[i] * num2[j] and add it to the current number in the product array  
    ```python
    product[i + j + 1] += num1[i] * num2[j]
    ```  
    b. Compute the carry for the next iteration and add it to the left of the current number  
    ```python
    product[i + j] += product[i + j + 1] // 10
    ```  
    c. Remove the carry from the current number and store the result  
    ```python
    product[i + j + 1] %= 10
    ```  
4. Remove the leading zeroes from the product array  
5. If needed, add the negative sign back to product[0]  
6. Return the product  
  
</br>  
  
Example if num1 = [1, 2, 3] and num2 = [3, 2, 1]:  
```
R = [0, 0, 0, 0, 0, 0]
R = [0, 0, 0, 0, 0, 3]
R = [0, 0, 0, 0, 6, 3]
R = [0, 0, 0, 9, 6, 3]
R = [0, 0, 0, 9, 8, 3]
R = [0, 0, 1, 3, 8, 3]
R = [0, 0, 7, 3, 8, 3]
R = [0, 0, 7, 4, 8, 3]
R = [0, 0, 9, 4, 8, 3]
R = [0, 3, 9, 4, 8, 3]
R = [3, 9, 4, 8, 3]
```  