# Reverse Bits

Problem:  
Write a program that reverses the bits of a given 64-bit unsigned integer.  
  
Example:    
```
 Input: 1110000000000001
Output: 1000000000000111
```  
  
Solution (from [reversebits-pythonicsol.py](reversebits-pythonicsol.py)): 
```python
def reverse_bits(x):
    return int(bin(x)[2:].zfill(64)[::-1], 2)
```  
  
Explanation: 
1. Reverse the bits  
```python
bin(x)[::-1]
```  
2. Remove the '0b' from the binary number  
```python
bin(x)[2:][::-1]
```  
3. Pad the binary number to 64 bits
```python
bin(x)[2:].zfill(64)[::-1]
```  
4. Convert the number from base 2 (binary) to base 10 (decimal integer)
```python
int(bin(x)[2:].zfill(64)[::-1], 2)
```  
5. 