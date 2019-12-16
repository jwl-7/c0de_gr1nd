# Compute a Gray Code
Given a nonnegative integer _n_, return the _n_-bit gray code sequence.

A Gray code is a binary numeral system where adjacent numbers in the sequence differ in a single bit.

## Example
```
 Input: 2
Output: [0, 1, 3, 2]
```

## Solution
```python
def gray_code(num_bits):
    if num_bits == 0:
        return [0]

    result = gray_code(num_bits - 1)
    for x in result[::-1]:
        result.append(x | 1 << num_bits - 1)
    return result
```

## Explanation
Let's look at how to generate _n_-bit Gray codes from a list of (_n_ - 1)-bit Gray codes:
1. Let the list of (_n_ - 1)-bit Gray codes = L1 and the reverse of L1 = L2
2. Prepend a bit of 0 to all the codes in L1
3. Prepend a bit of 1 to all the codes in L2
4. Concatenate L1 and L2 = list of _n_-bit Gray codes

## Code Dissection
1. Set the base case `gray_code(0) = [0]`
    ```python
    if num_bits == 0:
        return [0]
    ```
2. Initialize the result to `gray_code(n - 1)` so that we can process each list of (_n_ - 1)-bit Gray codes
    ```python
    result = gray_code(num_bits - 1)
    ```
3. Prepend a bit of 1 to all the codes in the reverse of _result_
    ```python
    for x in result[::-1]:
        result.append(x | 1 << num_bits - 1)
    ```
4. Return the _n_-bit Gray code sequence
    ```python
    return result
    ```