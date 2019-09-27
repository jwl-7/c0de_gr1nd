# Compute All Mnemonics for a Phone Number
Each digit, apart from 0 and 1, in a phone keypad corresponds to one of three or four letters of the alphabet, as show in the figure below. Since words are easier to remember than numbers, it is natural to ask if a 7 or 10-digit phone number can be represented by a word. For example, "2276696" corresponds to "ACRONYM" as well as "ABPOMZN".
```
-------------------
|     | ABC | DEF |
|  1  |  2  |  3  |
-------------------
| GHI | JKL | MNO |
|  4  |  5  |  6  |
-------------------
|PQRS | TUV |WXYZ |
|  7  |  8  |  9  |
-------------------
|     |     |     |
|  *  |  0  |  #  |
-------------------
```
Write a program which takes as input a phone number, specified as a string of digits, and returns all possible character sequences that correspond to the phone number. The cell phone keypad is specified by a mapping that takes a digit and returns the corresponding set of characters. The character sequences do not have to be legal words or phrases.
  
## Example
```
 Input: '47'
Output: ['GP', 'GQ', 'GR', 'GS', 'HP', 'HQ', 'HR', 'HS', 'IP', 'IQ', 'IR', 'IS']
```
  
## Solution
```python
def phone_mnemonic(phone_number):
    keypad = {
        '2': 'ABC',
        '3': 'DEF',
        '4': 'GHI',
        '5': 'JKL',
        '6': 'MNO',
        '7': 'PQRS',
        '8': 'TUV',
        '9': 'WXYZ',
    }
    mnemonics = ['']
    for num in phone_number:
        letters = keypad.get(num, num)
        mnemonics = [x+letter for x in mnemonics for letter in letters]
    return mnemonics
```
  
## Explanation
* BLANK
  
## Code Dissection
1. BLANK