# Computing the Parity of a Word
The parity of a binary word is 1 if the number of 1s in the word is odd; otherwise, it is 0. How would you compute the parity of a very large number of 64-bit words?  
  
## Examples
```
1011   -> 1
1001   -> 0
100100 -> 0
111000 -> 1
```
  
## Solution
```python
def parity(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1
```
  
## Explanation
* The XOR of two bits is 0 if both bits are 0 or both bits are 1  
* The XOR of a group of bits is its parity  
* The parity of 64-bit integer [_b<sub>63</sub>_, ... ,_b<sub>0</sub>_] = the parity of the XOR of [_b<sub>63</sub>_, ... ,_b<sub>32</sub>_] and [_b<sub>31</sub>_, ... ,_b<sub>0</sub>_]  
  
## Code Dissection
1. XOR two 32-bit values = parity of 64-bit operand  
    ```python
    x ^= x >> 32
    ```
2. XOR two 16-bit values = parity of 32-bit operand  
    ```python
    x ^= x >> 16
    ```
3. XOR two 8-bit values = parity of 16-bit operand  
    ```python
    x ^= x >> 8
    ```
4. XOR two 4-bit values = parity of 8-bit operand  
    ```python
    x ^= x >> 4
    ```
5. XOR two 2-bit values = parity of 4-bit operand  
    ```python
    x ^= x >> 2
    ```
6. XOR two 1-bit values = parity of 2-bit operand  
    ```python
    x ^= x >> 1
    ```
7. Extract the last bit to get the parity  
    ```python
    return x & 1
    ```
  
## Step-by-Step Example
Let x = 11010111  
```
1. 10110111
2. 10110111
3. 10110111
4. 10111100
5. 10010011
6. 11011010
7. 0
```
  
## Useful References
* [python Wiki - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)  
* [tutorialspoint - Bitwise Operators Example](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)