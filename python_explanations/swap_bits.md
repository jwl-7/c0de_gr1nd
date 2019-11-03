# Swap Bits
Given a 64-bit integer, swap the bits at indices _i_ and _j_.

## Example
* Let _x_ = 1234 in decimal
* Let _i_ = 3
* Let _j_ = 7

##### 1234 in binary viewed as an array of bits
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
1. Extract the _i_-th bit and _j_-th bit by shifting to the right
2. If the swap is necessary, flip the bits to swap

## Code Dissection
1. Extract the _i_-th bit
    ```python
    bit_i = x >> i & 1
    ```
2. Extract the _j_-th bit
    ```python
    bit_j = x >> j & 1
    ```
3. Check if the swap is necessary, which is if the bits are not equal to each other
    ```python
    if bit_i != bit_j:
    ```
4. Flip the _i_-th bit
    ```python
    x ^= 1 << i
    ```
5. Flip the _j_-th bit
    ```python
    x ^= 1 << j
    ```
6. Return the decimal number with the swapped bits
    ```python
    return x
    ```

## Useful References
* [Python Wiki - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
* [tutorialspoint - Bitwise Operators Example](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)