# Reverse Bits
Write a program that takes a 64-bit unsigned integer and returns the 64-bit unsigned integer consisting of the bits of the input in reverse order.  
  
## Example
* Let _x_ = 1110000000000001  
  
The bits in reverse order = 1000000000000111  
  
## Pythonic Solution
```python
def reverse_bits(x):
    return int(bin(x)[2:].zfill(64)[::-1], 2)
```
  
## Bit Manipulation Solution
```python
def reverse_bits(x):
    result = 0
    for i in range(64):
        result = (result << 1) + (x & 1)
        x >>= 1
    return result
```
  
## Explanation
* The fastest way to reverse the bits would be to build an array-based lookup, however, that would require much additional code and calculations unless hardcoded  
* 