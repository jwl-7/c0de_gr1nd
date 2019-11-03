# Is an Anonymous Letter Constructible?
Write a program which takes text for an anonymous letter and text for a magazine and determines if it is possible to write the anonymous letter using the magazine. The anonymous letter can be written using the magazine if for each character in the anonymous letter, the number of times it appears in the anonymous letter is no more than the number of times it appears in the magazine.

## Examples
```
 Input:   letter_text = 'aa'
        magazine_text = 'aaa'
Output: True

 Input:   letter_text = '12323'
        magazine_text = '123'
Output: False
```

## Solution
```python
def is_letter_constructible_from_magazine(letter_text, magazine_text):
    letter = collections.Counter(letter_text)
    for char in magazine_text:
        if char in letter:
            letter[char] -= 1
            if letter[char] == 0:
                del letter[char]
                if not letter:
                    return True
    return not letter
```

## Pythonic Solution
```python
def is_letter_constructible_from_magazine_pythonic(letter_text, magazine_text):
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)
```

## Explanation
* To construct the letter using the magazine, each character in the letter must also exist in the magazine for at least the same number of times

## Code Dissection
1. Create tables for each character/count in the letter and magazine
    ```python
    letter = collections.Counter(letter_text)
    magazine = collections.Counter(magazine_text)
    ```
    * The table structure is `{char: count}`
2. Iterate over each 

## Pythonic Code Dissection
1. BLANK