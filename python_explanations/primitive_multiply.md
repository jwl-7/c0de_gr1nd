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
  
Let's take a look at multiplying two binary numbers  
<pre><code>
              1 1 0 1
      &times; 1 0 1 1
                  ---
              1 1 0 1  (1101 &times; 1)
            1 1 0 1    (1101 &times; 1 shifted once)
          0 0 0 0      (1101 &times; 0 shifted twice)
 &plus; 1 1 0 1        (1101 &times; 1 shifted thrice)
                  ---
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