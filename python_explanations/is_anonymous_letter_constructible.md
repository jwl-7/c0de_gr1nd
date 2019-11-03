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
    magazine = collections.Counter(magazine_text)
    for char in letter:
        if char not in magazine.keys() or letter[char] > magazine[char]:
            return False
    return True
```

## Explanation
* BLANK

## Code Dissection
1. BLANK