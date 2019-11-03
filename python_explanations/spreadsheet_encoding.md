# Compute the Spreadsheet Column Encoding
Convert a spreadsheet column id to the corresponding integer. 'A' corresponds to 1.

## Examples
```
 Input: 'D'
Output:  4

 Input: 'AA'
Output:  27

 Input: 'ZZ'
Output:  702
```

## Solution
```python
def ss_decode_col_id(col):
    col_id = 0
    m = 1
    for char in col[::-1]:
        num = ord(char) - 64
        col_id += num * m
        m *= 26
    return col_id
```

## Explanation
* The problem is similar to converting a string representing a base-26 number to an integer, except that 'A' corresponds to 1 instead of 0
* The solution uses the function `ord('a')` to help return the desired integer for uppercase letters

## Code Dissection
1. Initialize a column id variable to store the result and a multiplier variable to help compute the id
    ```python
    col_id = 0
    m = 1
    ```
2. Loop through the input string backwards, and add the corresponding digit &times; multiplier to the result
    ```python
    for char in col[::-1]:
        num = ord(char) - 64
        col_id += num * m
        m *= 26
    ```
3. Return the computed column id
    ```python
    return col_id
    ```