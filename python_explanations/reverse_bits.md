# Reverse Bits
Given a 64-bit unsigned integer, reverse the order of the bits.

## Example
* Let _x_ = 1110000000000001

The bits in reverse order = 1000000000000111

## Bit Manipulation Solution
```python
def reverse_bits(x):
    j = 63
    for i in range(32):
        lsb = x >> i & 1
        msb = x >> j & 1
        if lsb != msb:
            x ^= 1 << i
            x ^= 1 << j
        j -= 1
    return x
```

## Pythonic Solution
```python
def reverse_bits(x):
    return int(bin(x)[2:].zfill(64)[::-1], 2)
```

## Explanation
* Iterate through the 32 least significant bits of the number, and swap each with the corresponding most significant bit

## Code Dissection
1. Define a variable that starts at 63 (the index of the most significant bit)
    ```python
    j = 63
    ```
2. Create a loop that will iterate over the 32 least significant bits
    ```python
    for i in range(32):
    ```
3. Extract the least significant bit at index _i_ and its corresponding most significant bit at index _j_
    ```python
    lsb = x >> i & 1
    msb = x >> j & 1
    ```
4. Check if the swap is necessary, which is if the bits are not equal to each other
    ```python
    if lsb != msb:
    ```
5. Flip the _i_-th bit
    ```python
    x ^= 1 << i
    ```
6. Flip the _j_-th bit
    ```python
    x ^= 1 << j
    ```
7. Decrement _j_ to keep the 32 most significant bits corresponding with the 32 least significant bits
    ```python
    j -= 1
    ```
8. Return the integer with the reversed bits
    ```python
    return x
    ```

## Pythonic Code Dissection
1. Use list comprehension to reverse the bits, pad the bits to the right with zeroes to bring the total amount of bits to 64, and return the integer with the reversed bits
    ```python
    return int(bin(x)[2:].zfill(64)[::-1], 2)
    ```
    Let's break down this cool line of code:
    * `bin(x)` converts the integer to a binary number, which looks like `0b0101010`
    * `[2:]` slices the binary number so that the first 2 characters are cut off, so that the number does not contain '0b'
    * `[::-1]` uses slice notation to reverse the bits of the binary number
    * `zfill(64)` pads the bits to the right of our reversed binary number with zeroes up to a total of 64 bits
    * `int(x, 2)` returns an integer constructed from _x_ with the base of the input number defined as 2

## Useful References
* [Python Wiki - Bitwise Operators](https://wiki.python.org/moin/BitwiseOperators)
* [tutorialspoint - Bitwise Operators Example](https://www.tutorialspoint.com/python/bitwise_operators_example.htm)