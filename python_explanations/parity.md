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
  
Explanation:
1. Initialize parity = 0  
2. Loop while x != 0  
    a. Invert parity   
    ```python
    result = not result
    ```  
    b. Erase lowest (rightmost) set bit   
    ```python
    x = x & (x - 1)
    ```  
3. Return the parity  
  
</br>  
  
[Python Bitwise Operators Reference](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)