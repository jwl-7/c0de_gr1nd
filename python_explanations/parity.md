# Computing the Parity of a Word
If a number has an odd number of 1-bits, then it has an odd parity. Conversely, if a number has an even number of 1-bits, then it has an even parity. Compute the parity of a 64-bit word.

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
* The XOR of two bits = 0 if both bits are 0 or 1
* The XOR of a group of bits is its parity

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
* Let _x_ = 11010111
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
* [Python Wiki - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
* [tutorialspoint - Bitwise Operators Example](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)