# Is an Anonymous Letter Constructible?
Given a string of characters for an anonymous letter and a string of characters for a magazine, determine whether or not the anonymous letter can be written using the magazine.

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
1. Create a table to hold each character/count in the letter
    ```python
    letter = collections.Counter(letter_text)
    ```
    * The table structure is `{char: count}`
2. Iterate through each character in the magazine and if it exists, decrement that character's count in the table
    ```python
    if char in letter:
        letter[char] -= 1
    ```
3. If the character count in the table drops to zero, remove it from the hash table, and check if the table is empty
    ```python
    if letter[char] == 0:
        del letter[char]
        if not letter:
            return True
    ```
    * If the hash table is empty, then every character in the letter also exists in the magazine
4. If we make it out of the loop, return whether or not the hash table is empty
    ```python
    return not letter
    ```

## Pythonic Code Dissection
1. Create a hash table for the letter and a hash table for the magazine, then subtract them and return whether or not the resulting table is empty
    ```python
    return not collections.Counter(letter_text) - collections.Counter(magazine_text)
    ```
    * For this statement, by subtracting the 2 tables, the result is 1 table
    * In the subtraction, only keys with positive counts are kept in the table
    * If every character in the letter exists in the magazine, then the result will be an empty hash table