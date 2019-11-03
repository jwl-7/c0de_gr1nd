# Find a Closest Integer with the Same Weight
The weight of a nonnegative integer is the number of 1-bits it has. Given a nonnegative integer _x_, find an integer _y_ with the same weight.

## Example
```
74 in binary = 1001010
The weight of 74 is 3.
The closest integer would be 73.
73 in binary = 1001001
The weight of 73 is also 3.
```

## Solution
```python
def closest_int_same_bit_count(x):
    for i in range(63):
        bit_i = x >> i & 1
        bit_j = x >> i + 1 & 1
        if bit_i != bit_j:
            x ^= 1 << i
            x ^= 1 << i + 1
            return x
```

## Explanation
1. Loop through all the bits, starting at the least significant bit &mdash; stop when the _i_-th bit and the bit to its left (_j_-th bit) differ
2. Swap the _i_-th and _j_-th bit, which preserves the weight

## Code Dissection
1. Iterate through all 64 bits
    ```python
    for i in range(63):
    ```
2. Extract the _i_-th bit, which starts at the least significant bit
    ```python
    bit_i = x >> i & 1
    ```
3. Extract the _j_-th bit, which is the bit to the left of the _i_-th bit
    ```python
    bit_j = x >> i + 1 & 1
    ```
4. Check if the _i_-th bit and _j_-th bit differ
    ```python
    if bit_i != bit_j:
    ```
5. Flip the _i_-th bit and _j_-th bit, which will make _x_ a different integer while preserving the same weight
    ```python
    x ^= 1 << i
    x ^= 1 << i + 1
    ```
6. Return the closest integer with the same weight
    ```python
    return x
    ```

## Useful References
* [Python Wiki - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
* [tutorialspoint - Bitwise Operators Example](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)