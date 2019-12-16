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
        result.append(x + (1 << num_bits - 1))
    return result
```

## Explanation
* BLANK

## Code Dissection
1. BLANK