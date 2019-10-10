# Implement Run-Length Encoding
Run-length encoding (RLE) compression offers a fast way to do efficient on-the-fly compression and decompression of strings. The idea is simple --- encode successive repeated characters by the repetition count and the character. For example, the RLE of "aaaabcccaa" is "4a1b3c2a". The decoding of "3e4f2e" returns "eeeffffee".  
  
Implement run-length encoding and decoding functions. Assume the string to be encoded consists of letters of the alphabet, with no digits, and the string to be decoded is valid encoding.
  
## Examples
```
Decoding:
    Input: '5a12z6n21y3d3p'
   Output: 'aaaaazzzzzzzzzzzznnnnnnyyyyyyyyyyyyyyyyyyyyydddppp'

Encoding:
    Input: 'vvvkkkkkkkkwwwwwwwwwwwwwwwwwffffffffffmmmmmmm'
   Output: '3v8k17w10f7m'
```
  
## Solution
```python
def decoding(s):
    decoded = ''
    count = ''
    for char in s:
        if char.isdigit():
            count += char
        else:
            decoded += int(count) * char
            count = ''
    return decoded


def encoding(s):
    encoded = ''
    prev = s[0]
    count = 0
    for char in s:
        if char == prev:
            count += 1
        else:
            encoded += str(count) + prev
            prev = char
            count = 1    
    encoded += str(count) + char
    return encoded
```
  
## Explanation
* Decoding - Iterate through the string, keep _count_ of the numeric characters, and when encountering an alphabetical character, add it _count_ times to the decoded string
* Encoding - Iterate through the string, keep _count_ of the number of consecutive character occurences, and when encountering a different character, add the _count_ and the character to the encoded string
* Both solutions share similar concepts, but decoding is much simpler
* The solution for encoding is similar to the solution for the look-and-say problem
  
## Code Dissection - decoding
1. Create two string variables to hold the _decoded_ string and the numeric characters
    ```python
    decoded = ''
    count = ''
    ```
2. Loop over each character in the encoded string
    ```python
    for char in s:
    ```
3. If the character is numeric, add it to _count_
    ```python
    if char.isdigit():
        count += char
    ```
    * Keeping _count_ a string saves us from doing more math in the case of multiple numeric characters in a row
4. If the character is alphabetical, add it _count_ times to the _decoded_ string and reset _count_
    ```python
    else:
        decoded += int(count) * char
        count = ''
    ```
    * Multiplying a character (or string) by an integer _n_ returns the character _n_ times
5. Return the decoded string
    ```python
    return decoded
    ```
  
## Code Dissection - encoding
1. Create variables to hold the _encoded_ string, the previous character, and keep track of consecutive occurrances of a character
    ```python
    encoded = ''
    prev = s[0]
    count = 0
    ```
2. Loop over each character in the string
    ```python
    for char in s:
    ```
3. If the current character is the same as the previous, increment _count_
    ```python
    if char == prev:
        count += 1
    ```
4. If the current and previous character are not the same, add the _count_ and previous character to the _encoded_ string
    ```python
    else:
        encoded += str(count) + prev
        prev = char
        count = 1
    ```
5. After breaking out of the loop, make sure to add the last _count_ and character to the _encoded_ string before returning it
    ```python
    encoded += str(count) + char
    return encoded
    ```