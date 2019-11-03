# Convert from Roman to Decimal
Given a string _s_ comprised of roman numerals, return the decimal integer.
* _I_ = 1
* _V_ = 5
* _X_ = 10
* _L_ = 50
* _C_ = 100
* _D_ = 500
* _M_ = 1000
* _I_ can immediately precede _V_ and _X_.
* _X_ can immediately precede _L_ and _C_.
* _C_ can immediately precede _D_ and _M_.

## Examples
```
 Input: 'LIX'
Output: 59

 Input: 'XVII'
Output: 17

 Input: 'XLVII'
Output: 47
```

## Solution
```python
def roman_to_integer(s):
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    result = 0
    prev = 0
    for char in s[::-1]:
        if roman[char] < prev:
            result -= roman[char]
        else:
            result += roman[char]
        prev = roman[char]
    return result
```

## Explanation
* The solution iterates over the Roman numerals from [right -> left] and follows 2 simple rules:
    1. When a symbol appears after a larger symbol, it is subtracted
    2. When a symbol appears before a larger symbol, it is added

## Code Dissection
1. Create a dictionary that maps the Roman numerals to their corresponding decimal values
    ```python
    roman = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    ```
2. Create variables to hold the result and the previous symbol's value
    ```python
    result = 0
    prev = 0
    ```
3. Loop over each symbol in the string from [right -> left]
    ```python
    for char in s[::-1]:
    ```
4. Rule #1 &mdash; When a symbol appears after a larger symbol, it is subtracted
    ```python
    if roman[char] < prev:
        result -= roman[char]
    ```
5. Implement Rule #2 &mdash; When a symbol appears before a larger symbol, it is added
    ```python
    else:
        result += roman[char]
    ```
6. Set the previous symbol to the current symbol for the next loop iteration
    ```python
    prev = roman[char]
    ```
7. Return the computed integer
    ```python
    return result
    ```