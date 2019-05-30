# Compute _x <sup>y</sup>_
Write a program that takes a double _x_ and an integer _y_ and returns _x <sup>y</sup>_. You can ignore overflow and underflow.  
  
## Examples
```
 Input: x = 9.871778445549765, y = 3
Output: 962.0246486149941

 Input: x = 1.0005205926241314, y = 2
Output: 1.001041456264943

 Input: x = 3.398860582608009, y = 4
Output: 133.45455538332973
```
  
## Solution
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
  
## Explanation
* The brute-force algorithm is to compute _x <sup>2</sup>_ = _x_ &times; _x_, then _x <sup>3</sup>_ = _x <sup>2</sup>_ &times; _x_, and so on  
* The algorithm is made more efficient by exploiting the properties of exponentiation  
* When _y_ is a power of 2, the multiplications can be iterated by squaring like _x_, _x <sup>2</sup>_, (_x <sup>2</sup>_) _<sup>2</sup>_  
* When _y_ is nonnegative, if the least significant bit of _y_ is 0, the result is (_x <sup>y &#8725; 2</sup>_) <sup>2</sup>  
* When _y_ is nonnegative, if the least significant bit of _y_ is 1, the result is _x_ &times; (_x <sup>y &#8725; 2</sup>_) <sup>2</sup>  
* When _y_ is negative, if the least significant bit of _y_ is 0, the result is (_1&#8725;x <sup>-y &#8725; 2</sup>_) <sup>2</sup>  
* When _y_ is negative, if the least significant bit of _y_ is 1, the result is _1&#8725;x_ &times; (_1&#8725;x <sup>-y &#8725; 2</sup>_) <sup>2</sup>  
  
## Code Dissection
