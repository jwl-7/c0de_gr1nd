# Convert from Roman to Decimal 
The Roman numeral representation of positive integers uses the symbols _I_, _V_, _X_, _L_, _C_, _D_, _M_. Each symbol represents a value, with _I_ being 1, _V_ being 5, _X_ being 10, _L_ being 50, _C_ being 100, _D_ being 500, and _M_ being 1000.  
  
In this problem we give simplified rules for representing numbers in this system. Specifically, we define a string over the Roman number symbols to be a valid Roman number string if symbols appear in nonincreasing order, with the following exceptions allowed:

* _I_ can immediately precede _V_ and _X_.
* _X_ can immediately precede _L_ and _C_.
* _C_ can immediately precede _D_ and _M_.

Back-to-back exceptions are not allowed, e.g., _IXC_ is invalid, as is _CDM_.  
  
A valid complex Roman number string represents the integer which is the sum of the symbols that do not correspond to exceptions; for the exceptions, add the difference of the larger symbol and the smaller symbol.  
  
For example, the strings "XXXXXIIIIIIIII", "LVIIII", and "LIX" are valid Roman number strings representing 59. The shortest valid complex Roman number string corresponding to the integer 59 is "LIX".  
  
Write a program which takes as input a valid Roman number string _s_ and returns the integer it corresponds to.

  
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
* BLANK
  
## Code Dissection
1. BLANK