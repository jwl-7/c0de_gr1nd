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
|<span style='font-weight:normal'></br>1</span>|<span style='font-weight:normal'>ABC</br>2</span>|<span style='font-weight:normal'>DEF</br>3</span>|
|:--------------------------------------------:|:-----------------------------------------------:|:-----------------------------------------------:|
|                  GHI</br>4                   |                    JKL</br>5                    |                    MNO</br>6                    |
|                 PQRS</br>7                   |                    TUV</br>8                    |                   WXYZ</br>9                    |
|                     </br>*                   |     &emsp;&emsp;&emsp;</br>0                    |                       </br>#                    |

Write a program which takes as input a phone number, specified as a string of digits, and returns all possible character sequences that correspond to the phone number. The cell phone keypad is specified by a mapping that takes a digit and returns the corresponding set of characters. The character sequences do not have to be legal words or phrases.
  
## Example
```
 Input: '47'
Output: ['GP', 'GQ', 'GR', 'GS', 'HP', 'HQ', 'HR', 'HS', 'IP', 'IQ', 'IR', 'IS']
```
  
## Iterative Solution
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
  
## Recursive Solution
```python
def phone_mnemonic_recursive(phone_number):
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
    
    def build_mnemonic(i):
        if i == len(phone_number):
            mnemonics.append(''.join(current))
        else:
            letters = keypad.get(phone_number[i], phone_number[i])
            for letter in letters:
                current[i] = letter
                build_mnemonic(i + 1)

    mnemonics = []
    current = [0] * len(phone_number)
    build_mnemonic(0)
    return mnemonics
```
  
## Explanation
* Both solutions enumerate all possible mnemonics for a number and will build the same mnemonics list
* The iterative solution is significantly faster by almost ~4x
  
## Iterative Code Dissection
1. Create a dictionary of a phone keypad with the numbers as the keys and the letters as the values
```python
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
```
2. Create the mnemonics list with a single empty string
    ```python
    mnemonics = ['']
    ```
    * The empty string will help us when building each mnemonic to avoid having to use the operation ```''.join()```
3. Loop over each number in the phone number and use the keypad dictionary and list comprehension to build the mnemonics
    ```python
    for num in phone_number:
        letters = keypad.get(num, num)
        mnemonics = [x+letter for x in mnemonics for letter in letters]
    ```
    * ```keypad.get(num, num)``` grabs the letters corresponding to the current number
    * If the number is not in the keypad dictionary, the number is the value returned
    * ```x+letter``` is a string concatenation operation
4. Return the mnemonics list
    ```python
    return mnemonics
    ```
  
## Recursive Code Dissection
1. Create a dictionary of a phone keypad with the numbers as the keys and the letters as the values
```python
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
```
2. Create a function that builds a mnemonic -- this will be called recursively
    ```python
    def build_mnemonic(i):
    ```
    * ```i``` represents the current index of the number

    a. Add the computed mnemonic to the list when we reach the end of the phone number
    ```python
    if i == len(phone_number):
        mnemonics.append(''.join(current))
    ```
    b. Build the mnemonic recursively using the keypad dictionary
    ```python
    else:
        letters = keypad.get(phone_number[i], phone_number[i])
        for letter in letters:
            current[i] = letter
            build_mnemonic(i + 1)
    ```
    * ```keypad.get(phone_number[i], phone_number[i])``` grabs the letters corresponding to the current number
    * If the number is not in the keypad dictionary, the number is the value returned
3. Declare the lists to hold the mnemonics and the current mnemonic
    ```python
    mnemonics = []
    current = [0] * len(phone_number)
    ```
4. Call the recursive function and then return the list of mnemonics when it has been built
    ```python
    build_mnemonic(0)
    return mnemonics
    ```
  
## Step-by-Step Example
Let's look at how the mnemonics list is logically built to further clarify how each solution works:
```
 Input: '47'

[0, 0]
['G', 0]
['G', 'P']
['G', 'Q']
['G', 'R']
['G', 'S']
['H', 'S']
['H', 'P']
['H', 'Q']
['H', 'R']
['H', 'S']
['I', 'S']
['I', 'P']
['I', 'Q']
['I', 'R']
['I', 'S']

Output: ['GP', 'GQ', 'GR', 'GS', 'HP', 'HQ', 'HR', 'HS', 'IP', 'IQ', 'IR', 'IS']
```