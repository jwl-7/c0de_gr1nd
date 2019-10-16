# Compute All Valid IP Addresses
Write a program that determines where to add periods to a decimal string so that the resulting string is a valid IP address. There may be more than one valid IP address corresponding to a string, in which case you should print all possibilities.

## Examples
```
 Input: '19216811'
Output: [
        '1.92.168.11',
        '19.2.168.11',
        '19.21.68.11',
        '19.216.8.11',
        '19.216.81.1',
        '192.1.68.11',
        '192.16.8.11',
        '192.16.81.1',
        '192.168.1.1'
    ]

 Input: '11000'
Output: ['1.10.0.0', '11.0.0.0']
```

## Solution
```python
def get_valid_ip_address(s):
    ips = []
    for a in range(1, 4):
        for b in range(a + 1, a + 4):
            for c in range(b + 1, b + 4):
                if 1 <= len(s) - c <= 3:
                    tmp = (s[:a], s[a:b], s[b:c], s[c:])
                    if all(int(x) <= 255 and str(int(x)) == x for x in tmp):
                        ips.append('.'.join(tmp))
    return ips
```

## Explanation
Let's look at the elements of a valid IP address:

1. Constructed of 4 decimal strings separated by 3 dots
2. All 4 substrings are between 0-255
3. All 3 dots are spaced 1-3 characters apart
4. Any substring longer than 1 character cannot start with a 0

Now let's look at the strategy the solution uses:
* All possible IP addresses can be found by enumerating all possible placements of the 3 dots
* Check each enumeration for validity by using the 4 rules stated above

## Code Dissection
1. Create an empty list to store the valid IP addresses
    ```python
    ips = []
    ```
2. Enumerate all possible placements of the 3 dots using nested loops
    ```python
    for a in range(1, 4):
        for b in range(a + 1, a + 4):
            for c in range(b + 1, b + 4):
    ```
    * _a_, _b_, and _c_ will represent the indexes to place each dot
    * Take note of the ```range(start, stop)``` arguments for the two inner loops
3. Now that we can enumerate the dot placements, let's make sure to skip over invalid dot placements
    ```python
    if 1 <= len(s) - c <= 3:
    ```
    * ```len(s) - c``` represents how many characters follow the third dot
    * Remember each substring in a valid IP address is 1-3 characters
4. If the dot placements seem valid, create a tuple with the 4 substrings
    ```python
    tmp = (s[:a], s[a:b], s[b:c], s[c:])
    ```
5. Check all 4 substrings in _tmp_ and add them to the list if they are valid
    ```python
    if all(int(x) <= 255 and str(int(x)) == x for x in tmp):
        ips.append('.'.join(tmp)
    ```
    * ```all(iterable)``` returns True if all the elements fit the condition
    * ```int(x) <= 255``` checks if any substring is too high of number
    * ```str(int(x)) == x``` checks for any leading zeroes
        * For example, ```str(int('00'))``` returns '0'
6. Return the list of valid IP addresses
    ```python
    return ips
    ```