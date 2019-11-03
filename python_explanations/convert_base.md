# Base Conversion
Given a string that represents a number, convert the number from the given base _b<sub>1</sub>_ to the base _b<sub>2</sub>. Use hex format.

## Examples
```
 Input: '615', 7, 13
Output: '1A7'

 Input: '-4AC', 12, 16
Output: '-2C4'

 Input: '-0', 4, 8
Output: '-0'
```

## Solution
```python
def convert_base(num_as_string, b1, b2):
    if num_as_string == '0' or num_as_string == '-0':
        return num_as_string

    is_negative = False
    if num_as_string[0] == '-':
        num_as_string = num_as_string[1:]
        is_negative = True

    num = 0
    for digit in num_as_string:
        num = num * b1 + int(digit, 16)

    digits = []
    while num > 0:
        digits.append(f'{int(num % b2):X}')
        num //= b2
    return ('-' if is_negative else '') + ''.join(digits[::-1])
```

## Explanation
* Convert the given number string to a decimal integer, then convert it to an integer in base _b<sub>2</sub>_

## Code Dissection
1. Return the number string if it equals '0' or '-0', since no conversion is needed
    ```python
    if num_as_string == '0' or num_as_string == '-0':
        return num_as_string
    ```
2. Check if the number string is negative, and remove the sign character if it is
    ```python
    is_negative = False
    if num_as_string[0] == '-':
        num_as_string = num_as_string[1:]
        is_negative = True
    ```
3. Convert the number string into a decimal integer one digit at a time
    ```python
    num = 0
    for digit in num_as_string:
        num = num * b1 + int(digit, 16)
    ```
    * `int(digit, 16)` converts a hex character such as 'A' to 10
4. Convert the computed decimal integer into an integer in base _b<sub>2</sub>_
    ```python
    digits = []
    while num > 0:
        digits.append(f'{int(num % b2):X}')
        num //= b2
    ```
    * `num % b2` computes a digit in the base _b<sub>2</sub>_
    * `:X` converts any numbers such as 10 to 'A'
5. Return the integer with the correct sign character
    ```python
    return ('-' if is_negative else '') + ''.join(digits[::-1])
    ```