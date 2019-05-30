# Swap Bits
A 64-bit integer can be viewed as an array of 64-bits, with the bit at index 0 corresponding to the least significant bit (LSB), and the bit at index 63 corresponding to the most significant bit (MSB). Implement code that takes as input a 64-bit integer and swaps the bits at indices _i_ and _j_.  
  
## Example
* Let _x_ = 1234 in decimal  
* Let _i_ = 3  
* Let _j_ = 7  
  
##### 1234 in binary represented by an array 
|MSB | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |LSB|
|---:|---|---|---|---|---|---|---|---|---|---|
|  1 | 0 | 0 | 1 | 1 | 0 | 1 | 0 | 0 | 1 | 0 |
  
##### Bits [3] and [7] (0 and 1) will be swapped
|MSB | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 |LSB|
|---:|---|---|---|---|---|---|---|---|---|---|
|  1 | 0 | 0 | 0 | 1 | 0 | 1 | 1 | 0 | 1 | 0 |
  
The swapped number in decimal = 1114  
  
## Solution
```python
def swap_bits(x, i, j):
    bit_i = x >> i & 1
    bit_j = x >> j & 1
    if bit_i != bit_j:
        x ^= 1 << i
        x ^= 1 << j
    return x
```
  
## Explanation
* 