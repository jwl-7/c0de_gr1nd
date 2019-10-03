# Compute _x_ &#8725; _y_
Given two positive integers, compute their quotient, using only the addition, subtraction, and shifting operators.  
  
## Examples
```
12 / 4 = 3
7 / 7  = 1
10 / 5 = 2
42 / 7 = 6
```
  
## Solution
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
  
## Explanation
* The brute-force algorithm is to iteratively subtract _y_ from _x_ until _x_ < _y_; the quotient is the number of subtractions  
  
## Code Dissection
1. Initialize the quotient to zero  
    ```python
    quotient = 0
    ```
2. Create an outer loop that runs until _x_ <= _y_, which stops when the quotient has been computed  
    ```python
    while x >= y:
    ```
3. Create a temporary _y_ and multiple variable that will help with optimizing the algorithm  
    ```python
    y2 = y
    multiple = 1
    ```
4. Create an inner loop that runs until _x_ < _y2_ &times; 2  
    ``` python
    while x >= y2 << 1:
    ```
5. Shift the multiple and _y2_ to the left once, which is equivalent to multiple *= 2 and _y2_ *= 2  
    ```python
    multiple <<= 1
    y2 <<= 1
    ```
6. Add the multiple to the quotient and subtract _y2_ from _x_  
    ```python
    quotient += multiple
    x -= y2
    ```
7. Return the quotient of _x_ &#8725; _y_  
    ```python
    return quotient
    ```
  
## Useful References
* [Python Wiki - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
* [tutorialspoint - Bitwise Operators Example](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)