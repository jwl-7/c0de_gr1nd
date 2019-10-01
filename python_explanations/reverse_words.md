# Reverse All the Words in a Sentence
Given a string containing a set of words separated by whitespace, we would like to transform it to a string in which the words appear in reverse order. We do not need to keep the original string.  
  
Implement a function for reversing the words in a string _s_. Assume _s_ is a string encoded as a bytearray.  
  
## Examples
```
 Input: 'Silence is peaceful'
Output: 'peaceful is Silence'

 Input: 'Alice likes Bob'
Output: 'Bob likes Alice'
```
  
## Solution
```python
def reverse_words(s):
    s[:] = s[::-1]
    start = 0
    while True:
        end = s.find(b' ', start)
        if end < 0:
            if start == 0:
                s[:] = s[::-1]
            else:
                s[start:] = s[end:start-1:-1]
            break
        if start < end:
            if start == 0:
                s[start:end] = s[end-1::-1]
            else:
                s[start:end] = s[end-1:start-1:-1]
        start = end + 1
```
  
## Pythonic Solution
```python
def reverse_words_pythonic(s):
    s[:] = b' '.join(word[::-1] for word in s[::-1].split(b' '))
```
  
## Explanation
* The solution reverses the string and then uses two pointers to reverse each word in the reversed string, whose indices are determined by finding the index of each whitespace character
    * This solution performs each operation in-place
* The pythonic solution uses list comprehension to generate a string with each word reversed in the reversed representation of the string
    * This solution is technically not in-place, as using built-in functions like ```str.split()``` create a new object, though they are usually temporary objects with references to the original that do not take up much space
    * Despite the fact that the pythonic solution theoretically has a higher time/space complexity, it performs significantly faster than the in-place solution
  
## Code Dissection
1. Reverse the string
    ```python
    s[:] = s[::-1]
    ```
2. Loop through the reversed string to reverse each word using a start and end pointer
    ```python
    start = 0
    while True:
        end = s.find(b' ', start)
    ```
    * ```start``` will represent the start index of a word
    * ```end``` will represent the end index of a word
    * ```s.find(b' ', start)``` returns the index of the first whitespace character after _start_
3. Loop until we have reached the end of the string
    ```python
    if end < 0:
    ```
    * ```s.find(b' ', start)``` will return -1 if no whitespace character is found

    1. When we reach the end of the string, be sure to reverse the last word before breaking out of the loop
        ```python
        if start == 0:
            s[:] = s[::-1]
        else:
            s[start:] = s[end:start-1:-1]
        break
        ```
        * ```if start == 0``` is the case that the string is one word without any whitespace characters, so we simply reverse the entire string again
        * ```else``` we need to reverse the last word in the string that occurs after a whitespace character
4. Reverse each word in the string during the loop
    ```python
    if start < end:
        if start == 0:
            s[start:end] = s[end-1::-1]
        else:
            s[start:end] = s[end-1:start-1:-1]
    start = end + 1
    ```
    * ```if start < end``` is the case that we are not at the last word
    * ```if start == 0``` is the case that we are at the first word
    * ```else``` we are at a word between the first and last word in the string
    * ```start = end + 1``` moves the start pointer to the next character so that the loop can find the next whitespace character
    * Note that while Python slicing notation follows the syntax ```a[start:stop:step]```, when using -1 to step backwards, it reverses the stop and start positions so that it follows the syntax ```a[stop:start:-1]```
  
## Pythonic Code Dissection
1. Use list comprehension and slice notation to reverse each word in the reversal of the string
    ```python
    s[:] = b' '.join(word[::-1] for word in s[::-1].split(b' '))
    ```
    Let's break this awesome line of code down:
    * ```s[::-1].split(b' ')``` returns a list of words in the reversal of the string with a whitespace character as the delimeter
        * ```b' '``` means we are defining the delimeter as a whitespace character in a bytearray object
    * ```word[::-1] for word in s[::-1]``` reverses each word in the reversal of the string
    * ```b' '.join``` joins each reversed word in the reversed list by a whitespace character to create the final string