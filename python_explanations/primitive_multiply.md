# Compute _x_ &times; _y_ Without Arithmetical Operators
Write a program that multiplies two nonnegative integers.  
The only operators you are allowed to use are:  
* assignment  
* the bitwise operators >>, <<, |, &, ~, ^  
* equality checks and Boolean combinations thereof  
  
## Examples
```
3 * 4  = 12
7 * 7  = 49
5 * 2  = 10
10 * 8 = 80
```
  
## Solution
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
  
## Explanation
* The algorithm is based off the grade-school method for multiplication, which uses shifting and adding  
* Since we cannot use arithmetical operators, we have to define our own addition function  
  
Let's take a look at multiplying two binary numbers using shifts and adds 
<pre><code>
              1 1 0 1
            &times; 1 0 1 1
      ----------------
              1 1 0 1  (1101 &times; 1)
            1 1 0 1    (1101 &times; 1 shifted once)
          0 0 0 0      (1101 &times; 0 shifted twice)
      &plus; 1 1 0 1        (1101 &times; 1 shifted thrice)
----------------------
                    1
                  1 1
                1 1 1
              1 1 0 1  (carry-out = 1)
            0 1 1 0 1  (carry-in = 1, carry-out = 1)
          0 0 1 1 0 1  (carry-in = 1, carry-out = 1)
        0 0 0 1 1 0 1  (carry-in = 1, carry-out = 1)
      1 0 0 0 1 1 0 1  (carry-in = 1)

Result of 1101 &times; 1011 = 10001101
</code></pre>
  
## Code Dissection - add
1. Create a loop that runs while _y_ != 0, which is the case when the sum has been computed  
    ```python
    while y != 0:
    ```
2. Set the carry to the common set bits of _x_ and _y_  
    ```python
    carry = x & y
    ```
3. Get the sum of bits _x_ and _y_  
    ```python
    x ^= y
    ```
4. Left shift the carry bit by 1, so that it gets carried into x in the next iteration  
    ```python
    y = carry << 1
    ```
5. Return the sum of _x_ and _y_  
    ```python
    return x
    ```
  
## Code Dissection - multiply
1. Initialize the product to zero  
    ```python
    product = 0
    ```
2. Create a loop that runs while _y_ != 0, which is the case when the product has been computed  
    ```python
    while y != 0:
    ```
3. If _y_ is odd, add _x_ to the product  
    ```python
    if y & 1:
        product = add(product, x)
    ```
4. Shift _x_ to the left once, which is equivalent to _x_ = _x_ &times; 2  
    ```python
    x <<= 1
    ```
5. Shift _y_ to the right once, which is equivalent to _y_ = _y_ &#8725; 2  
    ```python
    y >>= 1
    ```
6. Return the product of _x_ &times; _y_  
    ```python
    return product
    ```
  
## Useful References
* [python Wiki - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)  
* [tutorialspoint - Bitwise Operators Example](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)