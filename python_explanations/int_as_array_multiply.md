# Multiple Two Arbitrary-Precision Numbers
Given two arrays representing integers, multiply the two integers.

## Examples
```
[1, 2, 3] * [3, 2, 1] = [3, 9, 4, 8, 3]

[7, 0, 4, 9] * [1, 9, 8, 4] = [1, 3, 9, 8, 5, 2, 1, 6]

[1, 2, 3, 4, 5, 6, 7] * [7, 6, 5, 4, 3, 2, 1] = [9, 4, 4, 9, 7, 7, 2, 1, 1, 4, 0, 0, 7]
```

## Solution
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
            product[i+j+1] += num1[i] * num2[j]
            product[i+j] += product[i+j+1] // 10
            product[i+j+1] %= 10

    product = remove_leading_zeroes(product)
    if negative:
        product[0] = -product[0]
    return product
```

## Explanation
* The solution is based off the grade-school algorithm for multiplication, which is to multiply the first number by each digit of the second, then add up all the resulting terms

For instance, let's compute 123 &times; 321 using grade-school multiplication
1. 123 &times; 1 = 123
2. 123 &times; 2 &times; 10 = 2460
3. 123 &times; 3 &times; 100 = 36900
4. 123 &plus; 2460 &plus; 36900 = 39483

## Code Dissection - remove_leading_zeroes
1. Initialize variables to iterate through and to hold the size of the number
    ```python
    i = 0
    length = len(num) - 1
    ```
2. Loop over the number while the digit is zero
    ```python
    while i < length and num[0] == 0:
    ```
3. Remove the zero from the number, which will be at the start of the array
    ```python
    num.remove(0)
    i += 1
    ```
4. Return the number with the leading zeroes removed
    ```python
    return num
    ```

## Code Dissection - multiply
1. Check if the numbers at _num1_[0] and _num2_[0] are negative; if so, compute their absolute values
    ```python
    negative = False
    if num1[0] < 0 or num2[0] < 0:
        negative = True
        if num1[0] < 0 and num2[0] < 0:
            negative = False
        num1[0] = abs(num1[0])
        num2[0] = abs(num2[0])
    ```
2. Create an array to store the product, which will be at most _n_ + _m_ digits
    ```python
    product = [0] * len(num1 + num2)
    ```
3. Loop over both _num1_ and _num2_
    ```python
    for i in reversed(range(len(num1))):
        for j in reversed(range(len(num2))):
    ```
4. Multiply _num1_[_i_] &times; _num2_[_j_], then add the result to _product_
    ```python
    product[i+j+1] += num1[i] * num2[j]
    ```
5. Compute the carry for the next iteration and add it to the left of the current number
    ```python
    product[i+j] += product[i+j+1] // 10
    ```
6. Remove the carry from the current number and store the result
    ```python
    product[i+j+1] %= 10
    ```
7. Use the remove_leading_zeroes function to remove the leading zeroes from the product array
    ```python
    product = remove_leading_zeroes(product)
8. If the product is supposed to be negative, add the negative sign to the digit in _product_[0]
    ```python
    if negative:
        product[0] = -product[0]
    ```
9. Return the product of _num1_ &times; _num2_
    ```python
    return product
    ```

## Step-by-Step Example
* Let num1 = [1, 2, 3] and num2 = [3, 2, 1]
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